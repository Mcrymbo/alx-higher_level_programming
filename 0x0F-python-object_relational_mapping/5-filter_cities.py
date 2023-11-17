#!/usr/bin/python3
"""
Takes the name of the state as argument and list
the cities of that state
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}';".format(sys.argv[4]))
    cities = cur.fetchall()

    print(", ".join(city[0] for city in cities))
