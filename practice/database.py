import mysql.connector

config={
  'user': 'root',
  'password': 'Godev1',
  'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()