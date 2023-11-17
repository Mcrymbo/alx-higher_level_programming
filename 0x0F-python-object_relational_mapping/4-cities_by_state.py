#!/usr/bin/python3
"""
lists all cities from database
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, \
            states.name FROM cities JOIN states ON \
            cities.state_id = states.id;")
    cities = cur.fetchall()
    for city in cities:
        print(city)
