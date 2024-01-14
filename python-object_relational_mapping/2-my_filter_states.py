from sys import argv
import MySQLdb as Server

mysql_username, mysql_password, database_name, state_name = argv[1:]

config_connect = Server.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, database=database_name)

cursor = config_connect.cursor()

query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (state_name,))

rows = cursor.fetchall()

for row in rows:
    print(row)


