import sqlite3

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_name( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_name(col_fname,col_lname) VALUES (?,?)", \
        ("Tim","Calhoun"))
    cur.execute("INSERT INTO tbl_name(col_fname,col_lname) VALUES (?,?)", \
        ("Andrew","Calhoun"))
    cur.execute("INSERT INTO tbl_name(col_fname,col_lname) VALUES (?,?)", \
        ("Matt","Marqueef"))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname FROM tbl_name WHERE col_lname = 'Calhoun'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}".format(item[0],item[1])
        print(msg)
    
    


##    print(dir(sqlite3))
##    print(help(sqlite3))
