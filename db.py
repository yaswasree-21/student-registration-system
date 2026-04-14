import mysql.connector

db = mysql.connector.connect(host="Localhost",
                             user="root",
                             password="22f61a47I3",
                             database="registrationdb")
cursor = db.cursor()