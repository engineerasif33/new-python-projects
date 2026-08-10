import sqlite3
import os


connection = sqlite3.connect("school.db")

cursor = connection.cursor()
print("databse file")
print(os.path.abspath("school.db"))

#cursor.execute("""
#CREATE TABLE students3(
    #id INTEGER PRIMARY KEY,
    #name TEXT,
    #age INTEGER
#)
#""")

#print("database students3 and table is created successfully ")

# writing values in table
#cursor.execute("DROP TABLE IF EXISTS students")
#ursor.execute("DROP TABLE IF EXISTS students1")
#rsor.execute("DROP TABLE IF EXISTS students2")

#print("unncessary table deleted:")

    
while True:
    id = int(input("Enter ID: "))
    name =input("Enter Name: ")
    age = int(input("Enter Age: "))

    cursor.execute(
        "INSERT INTO students3 (id, name, age) VALUES (?, ?, ?)",
        (id, name, age)
    )

    choice = input("Do you want to add another student2? (y/n): ")

    if choice.lower() == "n":
        break

    print("values are inserted successfully ")

#updating record

cursor.execute(
    "update students3 set age = ? where name = ?",
 (10, "ibraim")
)
print("Database and table upadated successfully.")

   #delete record from any row
# cursor.execute("delete from students3 where id=1")
# print(" RECORD IS DELETED FROM ID 1")
  
# reading from table

cursor.execute("SELECT * FROM students3")

rows = cursor.fetchall()

for row in rows:
    print(row)
print("data is fetched and printed successfully")

connection.commit()

connection.close()


