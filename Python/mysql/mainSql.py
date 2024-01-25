import mysql.connector

#print(dir(mysql))

db = mysql.connector.connect(host='localhost',password='musaif',user='root', database='musaif')

name_values = ["musaif","sam","manu"]
if db.is_connected():
    print("connected successfully")

    cursor = db.cursor()
    # cursor.execute("DESCRIBE students;") # display all the properties of students table
    #cursor.execute("SHOW tables;")   # display existing tables
    #cursor.execute("SELECT * FROM students;")  # selecting the all the data from students table

    #cursor.execute("CREATE TABLE test(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50));")
    #cursor.execute("DESCRIBE test")
    for data in name_values:
        cursor.execute("INSERT INTO test(name) VALUES(%s)",[data])
    db.commit()  # data ko store karne keliye commit karna zaruri hai warna wo db me add nhi hoga
    cursor.execute("SELECT * FROM test;") 
    #print(cursor)
    for select in cursor:
        print(select)

else:
    raise ValueError