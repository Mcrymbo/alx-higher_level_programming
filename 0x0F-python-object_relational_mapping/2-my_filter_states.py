#!/usr/bin/python3
"""
Takes the name and display all values where in states
matches name in argument
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE CONVERT(`name` USING Latin1) \
                 COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
