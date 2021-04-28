import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="chorapaixao01")

mycursor = db.cursor()

mycursor.execute("show databases")


