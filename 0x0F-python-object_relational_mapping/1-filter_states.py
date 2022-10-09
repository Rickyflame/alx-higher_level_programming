#!/usr/bin/python3
"""
Lists all the states with a name starting wwith N from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM states
        WHERE name IS  NOT NULL
        AND LEFT(CAST(name AS BINARY), 1) ='N'
        ORDER BY states.id;
        """)
        records = cursor.fetchall()
        for record in records:
            print(record)
        db.close()
