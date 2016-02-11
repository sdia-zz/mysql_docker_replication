Mark
----


MySQL ETL based on binlog replication. Dumps to json files.

The dev environment consists of:


* MySQL docker container, configure as master and binlog type replica, row format

* genents.py allow insert/update events to MySQL,

* Mark.py connect to MySQL and dump to json

