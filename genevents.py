#!/usr/bin/env python                                                                                                                                                                                                
#-*- coding:utf-8 -*-                                                                                                                                                                                                

from __future__ import division
import random
import string
import time
from datetime import datetime
import pymysql



SPEED = 2


def get_message(size):
    s = ''
    chars = string.ascii_letters + string.digits + ' '
    for o in range(size):
        s += random.choice(chars)
    return s


def main():
    connection = pymysql.connect(
        host = '192.168.99.100',
        user='admin',
        password='mypass',
        db='scv')
    
    cursor = connection.cursor()

    while True:
        try:
            time.sleep(random.random() / SPEED)
            m = get_message(50)
            
            cursor.execute('INSERT INTO events (event) VALUES (%s)', m)
            connection.commit()
            print m

        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    main()
