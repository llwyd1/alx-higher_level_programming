#!/usr/bin/python3
"""Displays all values in the states table of a database"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = ("SELECT id, name FROM states WHERE name=%s")

    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
