#!/usr/bin/python3
"""
displays the list of ststes where the name is read from bash
safely
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states \
            WHERE name=%s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
