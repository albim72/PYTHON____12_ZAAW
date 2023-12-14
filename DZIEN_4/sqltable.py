import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='mojabazapython')

cursorObject = db.cursor()

tabela_student = ("CREATE TABLE IF NOT EXISTS student(firstname varchar(100),"
                  "lastname varchar(100),nrstudenta int primary key);")

cursorObject.execute(tabela_student)

dodaj_st = "INSERT INTO student(firstname,lastname,nrstudenta) values(%s,%s,%s);"
val_one = ("Jan","Kot",6868845)
cursorObject.execute(dodaj_st,val_one)

val_multi = [
    ("Maria","Wasek",55432),
    ("Olga","Kot",76576),
    ("Marek","Kos",35432),
    ("Nadia","Brok",8776832),
    ("Leon","Kowal",98732),
    ("Mira","Kuś",554372),
    ("Piotr","Besk",5535432),
    ("Eryk","Nowik",554732),
]

cursorObject.executemany(dodaj_st,val_multi)
db.commit()
db.close()
