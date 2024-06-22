#!/usr/bin/python3
"""Lists all states with a name starting with N from the database"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    try:

        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        sql = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC;"
        cur.execute(sql, ('N%',))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("{}".format(e))
    finally:
        cur.close()
        db.close()
