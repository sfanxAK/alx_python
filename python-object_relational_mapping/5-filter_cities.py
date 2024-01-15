import MySQLdb as Server
from sys import argv

config_connect = Server.connect(host='localhost', port='3306', user=argv[1], password=argv[2], database=argv[3])

cursor = config_connect.cursor()

cursor.execute("SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s)", (argv[4],))

rows = cursor.fetchall()

for row in rows:
    print(row)