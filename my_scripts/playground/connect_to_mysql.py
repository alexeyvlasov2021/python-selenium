import mysql.connector

# connect to database - check before writing below code
mydb = mysql.connector.connect(
    host = 'localhost',

    # this is default user when installing mysql server
    user = 'root',

    # this password set when install mysql server
    password = 'Vag007gt',

    # this port you can check in mysql workbench
    port = '3306',

    # the schema created
    database = 'python-demo'
)

my_cursor = mydb.cursor()

my_cursor.execute(
    'SELECT * FROM users'
)

# returns list of tuples
users = my_cursor.fetchall()

# iterate throw the list and print result
for user in users:
    # print(user)
    print(f"username: {user[1]}; password: {user[2]}")