from flask import Flask, render_template, request
import mysql.connector

cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='farm')
mycursor = cnx.cursor()
idcateg = 1;

app = Flask(__name__)



@app.route('/')
def index1():
    idcateg=1
    sql = "SELECT * FROM product where idcateg  = "+str(idcateg)+" ;"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    return render_template('index.html',products = products)


@app.route('/2')
def index2():
    idcateg=2
    sql = "SELECT * FROM product where idcateg  = "+str(idcateg)+" ;"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    return render_template('index.html',products = products)


@app.route('/3')
def index3():
    idcateg=3
    sql = "SELECT * FROM product where idcateg  = "+str(idcateg)+" ;"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    return render_template('index.html',products = products)

@app.route('/4')
def index4():
    idcateg=4
    sql = "SELECT * FROM product where idcateg  = "+str(idcateg)+" ;"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    return render_template('index.html',products = products)

if __name__ == "":
    app.run(debug=True)