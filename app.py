from flask import Flask
import mysql.connector
from flask import jsonify
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        connection = mysql.connector.connect(host='db',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        sql = ['CREATE DATABASE IF NOT EXISTS test', 'USE test', 'CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))']
        for query in sql:
            cursor.execute(query)
        sql = """INSERT INTO customers (name, address) VALUES (%s, %s)"""
        val = ("John", "Highway 21")
        cursor.execute(sql, val)
        connection.commit()
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify(data=result)
    except Error as e:
        return "Error reading data from MySQL table: {0}".format(e)


if __name__ == "__main__":
     app.run(debug=True,host='0.0.0.0')
