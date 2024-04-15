from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configure MySQL from environment variables

app.config['MYSQL_HOST'] = "mysql"
app.config['MYSQL_USER'] = os.environ['mysql_user']
app.config['MYSQL_PASSWORD'] = os.environ['mysql_password']
app.config['MYSQL_DB'] = os.environ['mysql_db']


# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def hello():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT * FROM messages')
        messages = cursor.fetchall()
    return render_template('index.html', messages=messages)

@app.route('/index', methods=['GET', 'POST'])
def index():
    new_message = request.form.get('new_message')
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
        mysql.connection.commit()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
