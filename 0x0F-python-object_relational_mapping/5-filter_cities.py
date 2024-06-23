#!/usr/bin/python3
"""lists all cities of a state taken as an argument of a database"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT cities.name from cities WHERE state_id="
    sql2 = "(SELECT states.id FROM states WHERE states.name=%s);"

    cur.execute(sql + sql2, (sys.argv[4],))
    rows = cur.fetchall()

    elem = []
    for row in rows:
        for col in row:
            elem.append(str(col))
    print(', '.join(elem))
