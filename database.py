import pymysql

conn = pymysql.connect(user='root', password='password', host='localhost')
cursor = conn.cursor()

try: cursor.execute("DROP DATABASE mydb;")
except: pass
cursor.execute("CREATE DATABASE mydb;")

conn.select_db("mydb")
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE users (
        id INT(11) NOT NULL AUTO_INCREMENT,
        email VARCHAR(255),
        password VARCHAR(255),
        PRIMARY KEY (id)
    );
    """)

except: 
    pass

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='mydb')

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT id,password FROM users WHERE email=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
