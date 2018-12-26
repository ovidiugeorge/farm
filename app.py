from flask import Flask, render_template, request
import mysql.connector

cnx = mysql.connector.connect(user = 'root', host = '127.0.0.1', database = 'farm')
mycursor = cnx.cursor()
app = Flask(__name__)
list = {}
credential = False
idperson = -1

def getTotalSum(list):
    sum = 0
    if list == {}:
        return 0
    else:
        for index in list:
            sum= sum+list[index][5]
    return sum

def getProd(idcateg):
    sql = "SELECT * FROM product where idcateg  = " + str(idcateg) + " ;"
    mycursor.execute(sql)
    return mycursor.fetchall()


@app.route('/checkout')
def checkout():
    global idperson, list
    print idperson
    sql = "SELECT count(*) FROM orders";
    mycursor.execute(sql)
    index = mycursor.fetchall()[0][0]
    total = getTotalSum(list)

    sql = "insert into orders values ("+ str(index) +", "+str(idperson)+","+str(total)+ ")"
    print sql
    mycursor.execute(sql)
    cnx.commit()
    for i in list:
        sql = "insert into sells values ("+ str(index) +", "+str(list[i][0])+")"
        print sql
        mycursor.execute(sql)
        #execute command
    cnx.commit()

    list = {}
    return render_template('finish.html')


def login() :
    return render_template('login.html')

@app.route('/logout')
def logOut() :
    global credential
    credential = False
    return render_template('login.html')


@app.route('/')
def index1():
    global credential
    if credential == False:
        return login()
    else:
        return render_template('index.html', products = getProd(1), page = 1)

@app.route('/2')
def index2():
    global credential
    if credential == False:
        return login()
    else:
        return render_template('index.html', products = getProd(2), page = 2)


@app.route('/3')
def index3():
    global credential
    if credential == False:
        return login()
    else:
        return render_template('index.html', products = getProd(3), page = 3)

@app.route('/4')
def index4():
    global credential
    if credential == False:
        return login()
    else:
        return render_template('index.html', products = getProd(4), page = 4)

@app.route('/shop', methods=['GET', 'POST'])
def addInCartShop():
    indexProd = int(request.args.get('number'))
    indexPage = int(request.args.get('page'))
    product = getProd(indexPage)[indexProd-1]
    list[len(list)] = product
    return option[indexPage]()

@app.route('/carts', methods=['GET', 'POST'])
def showProduct() :
    total = getTotalSum(list)
    return render_template('showListProduct.html', products = list, total= total)


@app.route('/remove', methods=['GET', 'POST'])
def removeProduct() :
    indexProd = int(request.args.get('number'))
    global list
    del list[indexProd]
    return showProduct()



@app.route('/login', methods=['GET', 'POST'])
def verifyLogin() :
    username = request.args.get('username')
    password = request.args.get('password')
    global credential, idperson
    sql = "SELECT count(*) FROM user where name  = '" + username + "' and password = '"+password+"';"
    mycursor.execute(sql)
    result = mycursor.fetchall()[0][0]

    if result == 1:
        credential = True

    sql = "SELECT iduser FROM user where name  = '" + username + "' and password = '"+password+"';"
    mycursor.execute(sql)
    idperson = mycursor.fetchall()[0][0]

    return index1()




option = {
    1 : index1,
    2 : index2,
    3 : index3,
    4 : index4
}

if __name__ == "":
    global list, option, credential, idperson
    app.run(debug = True)