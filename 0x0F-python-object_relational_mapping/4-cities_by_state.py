#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN "
    sql2 = "states on states.id = cities.state_id ORDER BY cities.id ASC;"
    cur.execute(sql + sql2)
    rows = cur.fetchall()
    for row in rows:
        print(row)
