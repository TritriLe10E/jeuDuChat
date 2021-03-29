from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '90.65.154.227'
app.config['MYSQL_USER'] = 'student'
app.config['MYSQL_PASSWORD'] = 'LDLC'
app.config['MYSQL_DB'] = 'kitty_crush'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


def sql_select(request):
    print("\n\n\n NEW SQL SELECT : " + request)
    cur = mysql.connection.cursor()
    cur.execute(request)
    rv = cur.fetchall()
    return rv

def sql_delete(request):
    print("\n\n\n NEW SQL DELETE : " + request)
    cur = mysql.connection.cursor()
    cur.execute(request)
    mysql.connection.commit()


def sql_insert(request):
    print("\n\n\n NEW SQL INSERT : " + request)
    cur = mysql.connection.cursor()
    cur.execute(request)
    mysql.connection.commit()
    cur.execute("SELECT LAST_INSERT_ID()")
    rv = cur.fetchall()
    print(rv)
    return rv[0]["LAST_INSERT_ID()"]

def sql_update(request):
    print("\n\n\n NEW SQL UPDATE : " + request)
    cur = mysql.connection.cursor()
    cur.execute(request)
    mysql.connection.commit()


from app import routes
