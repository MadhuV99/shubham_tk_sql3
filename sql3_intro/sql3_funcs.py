# sql3_intro using https://sqlitebrowser.org/
import sqlite3

conn = sqlite3.connect('mycompany.db')
curr = conn.cursor()

qry_stmt = "CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)"
print(qry_stmt)
curr.execute(qry_stmt)
conn.commit()

def sql_fetch():
    qry_stmt = "SELECT * FROM employees"   
    print(qry_stmt)
    curr.execute(qry_stmt)
    result_list = curr.fetchall()
    print(result_list)
    for record_tuple in result_list:
        print(record_tuple) 
        print(record_tuple[0]) 

def insert_value(id, name, salary, department, position):
    qry_stmt = 'INSERT INTO employees VALUES(?, ?, ?, ?, ?)' # each '?' is a place holder for a value 
    values_tuple = (id, name, salary, department, position) # a tuple of values corresponding to above '?'s
    print(qry_stmt, values_tuple)
    curr.execute(qry_stmt,values_tuple)
    conn.commit()


def update_department(dep, id):
    qry_stmt = 'UPDATE employees SET department=? WHERE id=?' # each '?' is a place holder for a value 
    values_tuple = (dep, id) # a tuple of values corresponding to above '?'s
    print(qry_stmt, values_tuple)
    curr.execute(qry_stmt,values_tuple)
    conn.commit()

def delete_all():
    qry_stmt = 'DELETE FROM employees' # Zap table (Delete ALL records from the Table) 
    print(qry_stmt)
    curr.execute(qry_stmt)
    conn.commit()

# insert_value(6, "Maxam", 80000, 'Python', 'Manager')

# update_department("JavaScript", 6)

# delete_all()
sql_fetch()

curr.close()
conn.close()

