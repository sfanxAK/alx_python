from sys import argv
import MySQLdb as Server

config_connect = Server.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

cursor = config_connect.cursor()

query1 = ("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]))

cursor.execute(query1, (state_name,))

rows = cursor.fetchall()

for row in rows:
    if row[1][0] == 'N':
        print(row)
