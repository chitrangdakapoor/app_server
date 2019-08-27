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

        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify(data=result)
    except Error as e:
        return "Error reading data from MySQL table: {0}".format(e)


if __name__ == "__main__":
     app.run(debug=True,host='0.0.0.0')
