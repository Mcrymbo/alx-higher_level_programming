#!/usr/bin/python3
""" This is s scrip for listing all states from a database """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for i in states:
        print(i)
