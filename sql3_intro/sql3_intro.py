# sql3_intro using https://sqlitebrowser.org/
import sqlite3

conn = sqlite3.connect('mycompany.db')
curr = conn.cursor()

qry_stmt = "CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)"
print(qry_stmt)
# curr.execute(qry_stmt)
# conn.commit()

qry_stmt = 'INSERT INTO employees VALUES(1, "Max Vax", 75000, "Python", "Developer")' # simple INSERT query open to SQL injection attack 
print(qry_stmt)
# curr.execute(qry_stmt)
# conn.commit()


qry_stmt = 'INSERT INTO employees VALUES(?, ?, ?, ?, ?)' # each '?' is a place holder for a value 
values_tuple = (2, "Sax Lax", 50000, "JS", "Developer") # a tuple of values corresponding to above '?'s
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt,values_tuple)
# conn.commit()

qry_stmt = 'INSERT INTO employees VALUES(?, ?, ?, ?, ?)' 
values_tuple = (3, "John", 80000, "Python", "Developer") 
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt,values_tuple)
values_tuple = (4, "Shane", 70000, "JavaScript", "Developer") 
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt,values_tuple)
values_tuple = (5, "Shane", 75000, "Ruby", "Developer") 
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt,values_tuple)
# conn.commit()


qry_stmt = "UPDATE employees SET department='Python' WHERE id=2" # simple UPDATE query open to SQL injection attack  
print(qry_stmt)
# curr.execute(qry_stmt)
# conn.commit()

qry_stmt = 'UPDATE employees SET department=? WHERE id=?' # each '?' is a place holder for a value 
values_tuple = ("PHP", 2) # a tuple of values corresponding to above '?'s
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt,values_tuple)
# conn.commit()

qry_stmt = "SELECT * FROM employees"   
print(qry_stmt)
curr.execute(qry_stmt)
result_list = curr.fetchall()
print(result_list)
for record_tuple in result_list:
    print(record_tuple) 
    print(record_tuple[1]) 

# qry_stmt = "SELECT name FROM employees WHERE salary > 60000"   
# print(qry_stmt)
# curr.execute(qry_stmt)
# result_list = curr.fetchall()
# print(result_list)
# for record_tuple in result_list:
#     print(record_tuple) 
#     print(record_tuple[0]) 

# qry_stmt = "SELECT name, salary FROM employees WHERE department=='Python'"   
# print(qry_stmt)
# curr.execute(qry_stmt)
# result_list = curr.fetchall()
# print(result_list)
# for record_tuple in result_list:
#     print(record_tuple) 
#     print(record_tuple[0]) 

qry_stmt = 'DELETE FROM employees WHERE name=? AND department=?' # each '?' is a place holder for a value 
values_tuple = ("Shane", 'JavaScript') # a tuple of values corresponding to above '?'s
print(qry_stmt, values_tuple)
# curr.execute(qry_stmt, values_tuple)
# conn.commit()

qry_stmt = 'DELETE FROM employees' # Zap table (Delete ALL records from the Table) 
print(qry_stmt)
# curr.execute(qry_stmt)
# conn.commit()


curr.close()
conn.close()

