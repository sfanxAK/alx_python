import MySQLdb as Server

config_connect = Server.connect(host="localhost", port=3306, user="alx_learner", passwd="alx01", db="hbtn_0e_0_usa")

cursor = config_connect.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()

for state in states:
    print(state)



