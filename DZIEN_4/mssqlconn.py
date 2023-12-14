import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-K4JE02F;DATABASE=autokomis;Trusted_Connection=yes')

cursor = conn.cursor()
cursor.execute("SELECT @@version;")
tu = cursor.fetchall()
print(tu)
