#!/usr/bin/python3
"""Script to select all rows in the states table"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db_info = sys.argv[1:]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=db_info[0],
        passwd=db_info[1],
        db=db_info[2],
        charset='utf8'
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors and databases
    cur.close()
    db.close()
