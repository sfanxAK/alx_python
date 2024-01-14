from sys import argv
import MySQLdb as Server

config_connect = Server.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

cursor = config_connect.cursor()

cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]))
cursor.execute(query, (state_name,))

rows = cursor.fetchall()

for row in rows:
    print(row)

