#! /usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb

__author__ = 'teppei'
def upsert_new_user(user_id,name):
    con = MySQLdb.connect(db="hatch",host="localhost",user="root")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("INSERT IGNORE INTO users (user_id,name) values (%s,%s)",
                (user_id,name))
    con.commit()



def main():
    print "Hello"


if __name__ == "__main__":
    main()
