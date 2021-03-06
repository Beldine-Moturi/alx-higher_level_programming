#!/usr/bin/python3
"""join tables"""


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
        "SELECT cities.name\
 FROM cities\
 INNER JOIN states\
 ON cities.state_id = states.id\
 WHERE states.name LIKE BINARY %s\
 ORDER BY cities.id ASC;", (db_info[3], ))

    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))

    cur.close()
    db.close()
