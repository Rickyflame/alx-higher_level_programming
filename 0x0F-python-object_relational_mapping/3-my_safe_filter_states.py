#!/usr/bin/python3
"""
A script that thakes in an argument and display all values in the states table
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
        WHERE CAST(name AS BINARY) = CAST('{}' AS BINARY)
        ORDER BY states.id;""".format(sys.argv[4]))
    records = cursor.fetchall()
    for record in records:
        print(record)
    db.close()
