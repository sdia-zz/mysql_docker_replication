#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os, time, json, copy, datetime
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)



mysql_settings = {'host': '192.168.99.100', 'port': 3306, 'user': 'admin', 'passwd': 'mypass'}
current_micro_time = lambda: int(time.time() * 1e6)
json_file_folder = '/tmp/'


def get_rows():    
    stream = BinLogStreamReader(connection_settings = mysql_settings,
                                server_id=1,
                                blocking=True,
                                resume_stream=True,
                                log_file='mysql-bin.000001',
                                log_pos=12169025,
                                only_events=[WriteRowsEvent,
                                             UpdateRowsEvent])
    for binlogevent in stream:
        metadata = dict(
            schema = binlogevent.schema,
            table = binlogevent.table,
            operation_time = current_micro_time())

        for row in binlogevent.rows:
            if isinstance(binlogevent, WriteRowsEvent):
                values = row['values'] # this is a dict
            elif isinstance(binlogevent, UpdateRowsEvent):
                values = row['after_values']
            
            yield dict(
                metadata = metadata,
                payload = values)
            
    stream.close()




def process_row(r):
    # datetime.datetime is not json serializable
    rc = copy.deepcopy(r)

    for k,v in r['payload'].iteritems():
        if isinstance(v, datetime.datetime):
            rc['payload'][k] = v.strftime('%Y-%m-%d %H:%M:%S')

    return rc




def dump_to_file(r):
    schema = r['metadata']['schema']
    table = r['metadata']['table']
    fpath = os.path.join(json_file_folder, '{}_{}.csv'.format(schema, table))
    if not os.path.isfile(fpath):
        mode = 'w'
    else:
        mode = 'a'
    with open(fpath, mode) as f:
        f.write('{}\n'.format(json.dumps(r)))
    


if __name__ == '__main__':
    for r in get_rows():
        dump_to_file(process_row(r))
