#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
if __name__ == "__main__"
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id"")
    row = cur.fetchall()
    for row in rows
        print(row)
    cur.close()
    db.close()
