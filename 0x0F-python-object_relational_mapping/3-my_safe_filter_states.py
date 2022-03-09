#!/usr/bin/python3
"""select all states with name matching a certain string-- safely"""


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
    cur.execute(
        "SELECT * FROM states\
            WHERE name=%s\
            ORDER BY id ASC;", (db_info[3]), )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
