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
def get_user(user_id):
    (con,cur)=get_con_cur()
    cur.execute("SELECT * from users where user_id = %s",(user_id))
    return cur.fetchone()
def get_con_cur():
    con = MySQLdb.connect(db="hatch",host="localhost",user="root")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    return con,cur
def cheer_count(egg_id):
    (con,cur) = get_con_cur()
    cur.execute("SELECT COUNT(DISTINCT user_id) from cheers where egg_id=%s",(egg_id))
    count = cur.fetchall()[0]["COUNT(DISTINCT user_id)"]
    return count

def main():
    print "Hello"


if __name__ == "__main__":
    main()
