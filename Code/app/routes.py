from flask import Response, render_template, url_for, flash, redirect, request, jsonify, make_response
from app import app, db, bcrypt
from app.forms import LoginForm,RegistrationForm
from app.models import Users
from app.recommend import recommendations
from app.sellerforecast import sforecast
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd
import json
from functools import reduce
from datetime import datetime, timedelta
import random
import os
import subprocess


@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		cur = db.connection.cursor()
		cur.execute(''' SELECT * FROM Users WHERE Usersname='{}' '''.format(form.username.data))
		r1 = cur.fetchone()
		if r1 and r1['Password']==form.password.data:
			user = Users.get_user(username=r1['Usersname'])
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if user.type=='c':
				return redirect(next_page) if next_page else redirect(url_for('home'))
			else:
				return redirect(url_for('seller_home'))
		else:
			flash('Login Unsuccessful. Check username/password.','danger')
	return render_template('landing.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	cur = db.connection.cursor()
	form = RegistrationForm()
	if form.validate_on_submit():
		sql1="INSERT INTO Users VALUES ('{}','{}','c')".format(form.username.data,form.password.data)
		cur.execute(sql1)
		sql2="INSERT INTO Customer(Fname,Lname,Ph_no,E_mail,Address,Pin,Usersname) VALUES ('{}','{}','{}','{}','{}',{},'{}')".format(form.fname.data,form.lname.data,form.phonenumber.data,form.email.data,form.address.data,form.pin.data,form.username.data)
		cur.execute(sql2)
		db.connection.commit()
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/home')
@login_required
def home():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	query = "SELECT prod_id FROM product"
	cur.execute(query)
	res = list(cur.fetchall())
	random.shuffle(res)
	result = res[1:6]
	result1 = res[7:12]
	result2 = res[13:18]
	print(result)
	if len(result)==0:
		return render_template('temp.html',title="No Categories Exist")
	return render_template('home.html', prods= result, prods1=result1, prods2=result2)


@app.route('/temp')
@login_required
def temp():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	return render_template('template.html')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/category')
@login_required
def all_category():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	query = "SELECT Name FROM Category"
	cur.execute(query)
	result = cur.fetchall()
	if len(result)==0:return render_template('temp.html',title="No Categories Exist")
	return render_template('category.html',rows = result)

@app.route("/category/<cat_name>")
def category(cat_name):
	if current_user.type=='s':return redirect(url_for('seller_home'))
	return render_template('cat_prod.html',title=cat_name,key=cat_name)

@app.route("/category_api")
def category_api():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	key = request.args.get('key')
	cur = db.connection.cursor()
	query = "SELECT * FROM product WHERE category_id IN (SELECT category_id from category WHERE Name='{}')".format(key)
	cur.execute(query)
	result = list(cur.fetchall())
	for i in result:
		i['Price']=float(i['Price'])
		i['Discount']=float(i['Discount'])
		i['Fprice']=i['Price']*(1-(i['Discount']/100))
	return make_response(jsonify(result)),200


@app.route("/search",methods=['GET'])
def search():
	key = request.args.get('key')
	return render_template('search.html',title="Search Result for '{}'".format(key),key=key)

@app.route("/search_api",methods=['GET'])
def search_api():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	key = request.args.get('key')
	cur = db.connection.cursor()
	query = "SELECT * FROM product WHERE Name LIKE '%{0}%' OR Brand LIKE '%{0}%' OR Description LIKE '%{0}%' ORDER BY Name ASC".format(key)
	cur.execute(query)
	result = list(cur.fetchall())
	for i in result:
		i['Price']=float(i['Price'])
		i['Discount']=float(i['Discount'])
		i['Fprice']=i['Price']*(1-(i['Discount']/100))
	return make_response(jsonify(result)),200

@app.route("/search/autocomplete/<key>")
def autocomplete(key):
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	query = "SELECT Name FROM product WHERE Name LIKE '%{0}%' ORDER BY Name ASC".format(key)
	cur.execute(query)
	result = cur.fetchall()
	arr = [i['Name'] for i in result]
	if len(arr)>6:
		arr = arr[:5]
	print(arr)
	return make_response(jsonify(arr)),200

@app.route("/all-products")
def all_products():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	return render_template('all_prod.html',title="All Products")

@app.route("/all-products-api")
def all_products_api():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	query = "SELECT * FROM product ORDER BY Name ASC"
	cur.execute(query)
	result = list(cur.fetchall())
	for i in result:
		i['Price']=float(i['Price'])
		i['Discount']=float(i['Discount'])
		i['Fprice']=i['Price']*(1-(i['Discount']/100))
	return make_response(jsonify(result)),200

@app.route("/product/<pid>")
def product(pid):
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	query = "SELECT * FROM product WHERE prod_id = {}".format(pid)
	cur.execute(query)
	result = cur.fetchone()
	if result:title=result['Name']
	else: return render_template('temp.html',title="Product Not Found")
	cur.execute("select count(*) as Likes from views where likes=1 and prod_id={}".format(pid))
	likes=cur.fetchone()['Likes']
	cur.execute("select count(*) as Dislikes from views where likes=0 and prod_id={}".format(pid))
	dislikes=cur.fetchone()['Dislikes']
	lstat=0
	cur.execute("select likes from views where Prod_id={} and Cust_id={}".format(pid,current_user.userid))
	temp=cur.fetchone()
	if temp: lstat= 1 if temp['likes'] else 2
	cur.execute("select avg(ratings) as rtng from reviews where Prod_id={}".format(pid))
	ratings = cur.fetchone()['rtng']
	if ratings is None:ratings=0
	cur.execute("select * from reviews where prod_id={} order by Rdate desc".format(pid))
	reviews = cur.fetchall()
	return render_template('product.html',row = result,title=title,likes=likes,dislikes=dislikes,lstat=lstat,ratings=ratings,reviews=reviews)

@app.route("/recommend",methods=['GET'])
def recommend():
	pid = request.args.get('pid')
	a = list()
	cur = db.connection.cursor()
	cur.execute("SELECT Cust_id,Prod_id FROM Views WHERE Likes = 1")
	result = cur.fetchall()
	if result:a.extend(result)
	cur.execute("SELECT Cust_id,Prod_id FROM Cart")
	result = cur.fetchall()
	if result:a.extend(result)
	cur.execute("SELECT o.Cust_id AS Cust_id,od.Prod_id AS Prod_id FROM Orders as o JOIN Orders_Details as od ON o.Orders_id=od.Orders_id")
	result = cur.fetchall()
	if result:a.extend(result)
	df = pd.DataFrame(a)
	x = recommendations(df,pid)
	x = list(set(x))
	x = [int(i) for i in x]
	print(x)
	return make_response(jsonify(x)),200

@app.route("/prodinfo/review",methods=['GET'])
def post_review():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	pid = request.args.get('prod_id')
	rt = request.args.get('rt')
	rv = request.args.get('rv')
	cid = current_user.userid
	cur = db.connection.cursor()
	cur.execute("DELETE FROM Reviews WHERE Prod_id={} and Cust_id={}".format(pid,cid))
	cur.execute("INSERT INTO Reviews values({},'{}',curdate(),{},{})".format(rt,rv,cid,pid))
	db.connection.commit()
	cur.execute("SELECT * from Reviews WHERE Prod_id={} AND Cust_id={} ".format(pid,cid))
	item = cur.fetchone()
	res = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(item['Ratings'],item['Rdate'],item['Description'])
	return res,200

@app.route("/prodinfo/likeop",methods=['GET'])
def likeop():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	pid = request.args.get('pid')
	op = request.args.get('op')
	cid = current_user.userid
	cur = db.connection.cursor()
	if(op=='1'):
		cur.execute("DELETE FROM views WHERE Prod_id={} and Cust_id={}".format(pid,cid))
		cur.execute("INSERT INTO views values(1,{},{})".format(cid,pid))
	if(op=='2'):
		cur.execute("DELETE FROM views WHERE Prod_id={} and Cust_id={}".format(pid,cid))
		cur.execute("INSERT INTO views values(0,{},{})".format(cid,pid))
	if(op=='3' or op=='4'):
		cur.execute("DELETE FROM views WHERE Prod_id={} and Cust_id={}".format(pid,cid))
	db.connection.commit()
	cur.execute("select count(*) as Likes from views where likes=1 and prod_id={}".format(pid))
	likes=cur.fetchone()['Likes']
	cur.execute("select count(*) as Dislikes from views where likes=0 and prod_id={}".format(pid))
	dislikes=cur.fetchone()['Dislikes']
	dict = {'likes':str(likes),'dislikes':str(dislikes)}
	return jsonify(dict),200

@app.route("/prodinfo/stock",methods=['GET'])
def get_stock():
	pid = request.args.get('pid')
	cur = db.connection.cursor()
	cur.execute("SELECT Price,Discount,Stock FROM product WHERE prod_id = {}".format(pid))
	result = cur.fetchone()
	if result is None:return "0",200
	fprice=result['Price']*(1-result['Discount']/100)
	result['Fprice']=float(fprice)
	result['Price']=float(result['Price'])
	result['Discount']=float(result['Discount'])
	result['Stock']=int(result['Stock'])
	print(result)
	print(jsonify(result))
	return make_response(jsonify(result)),200

@app.route("/cart",methods=['GET'])
def get_cart():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	query = "SELECT p.Prod_id as Prod_id,Name,Quantity,Amount FROM cart as c JOIN product as p ON p.Prod_id=c.Prod_id WHERE Cust_id={}".format(cid) 
	cur.execute(query)
	result = cur.fetchall()
	total = sum([i['Amount'] for i in result])
	message = request.args.get('message')
	return render_template('cart.html',rows = result,total = total,message=message)

@app.route("/cart/add",methods=['GET'])
def add_cart():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cur = db.connection.cursor()
	pid = request.args.get('pid')
	qty = int(request.args.get('qty'))
	cid = current_user.userid
	q1="SELECT * FROM product WHERE Prod_id={}".format(pid)
	cur.execute(q1)
	r1 = cur.fetchone()
	stock = r1['Stock']
	pname = r1['Name']
	dprice = r1['Price']*(1-(r1['Discount']/100))
	q2 = "SELECT * FROM cart WHERE Prod_id={} AND Cust_id={}".format(pid,cid)
	cur.execute(q2)
	r2 = cur.fetchone()
	query = "INSERT INTO cart VALUES({},{},{},{})"
	if r2 is not None:
		qty = qty+r2['Quantity']
		query = "UPDATE cart SET Quantity={} ,Amount={} WHERE Cust_id={} AND Prod_id={}"
	if qty<=stock:
		tprice = qty*dprice
		cur.execute(query.format(qty,tprice,cid,pid))
		db.connection.commit()
		return "Successfully Added To Cart",200
	else:
		return 400
	
@app.route("/cart/clear",methods=['GET'])
def clear_cart():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	query="DELETE FROM cart WHERE Cust_id={}".format(cid)
	cur = db.connection.cursor()
	cur.execute(query)
	db.connection.commit()
	return redirect(url_for("get_cart"))

@app.route("/cart/confirm",methods=['GET'])
def confirm_cart():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	wallet=0
	query="SELECT SUM(Amount) AS Balance FROM Wallet WHERE Cust_id={}".format(cid)
	cur.execute(query)
	result = cur.fetchone()
	print(result)
	if result['Balance'] is not None:
		wallet = result['Balance']
	query="SELECT SUM(Amount) as t,SUM(Quantity) as q FROM Cart WHERE Cust_id={}".format(cid)
	cur.execute(query)
	result = cur.fetchone()
	total = result['t']
	print(total)
	count = result['q']
	if total>wallet:
		return redirect(url_for("get_cart",message="Insufficient Wallet Balance!"))	
	else:
		cur.execute("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'ec' AND TABLE_NAME = 'Orders'")
		orders_id = cur.fetchone()['AUTO_INCREMENT']
		cur.execute("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'ec' AND TABLE_NAME = 'Wallet'")
		txn_id = cur.fetchone()['AUTO_INCREMENT']
		cur.execute("Insert into Wallet(Amount,Type,Tdate,Cust_id) values({},'Dr',curdate(),{})".format(-total,cid))
		cur.execute("Insert into Orders(OrdersDate,Status,N_items,TotalAmt,Cust_id,Txn_id) values(curdate(),'Pending',{},{},{},{})".format(count,total,cid,txn_id))
		cur.execute("SELECT * from Cart WHERE Cust_id={}".format(cid))
		result = cur.fetchall()
		for row in result:  
			cur.execute("INSERT INTO Orders_Details VALUES({},{},{},{})".format(row['Quantity'],row['Amount'],orders_id,row['Prod_id']))
			cur.execute("SELECT Stock FROM Product WHERE Prod_id={}".format(row['Prod_id']))
			qval = cur.fetchone()['Stock']-row['Quantity']
			cur.execute("UPDATE Product SET Stock={} WHERE Prod_id={}".format(qval,row['Prod_id']))
		cur.execute("DELETE FROM Cart WHERE Cust_id={}".format(cid))
		db.connection.commit()
		return redirect(url_for("order_det",oid=orders_id))

@app.route("/cart/remove",methods=['GET'])
def remove_cart():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	pid = request.args.get('pid')
	query="DELETE FROM cart WHERE Cust_id={} AND Prod_id={}".format(cid,pid)
	cur = db.connection.cursor()
	cur.execute(query)
	db.connection.commit()
	return str(pid),200

@app.route("/order_details/<oid>",methods=['GET'])
def order_det(oid):
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	cur.execute("SELECT * FROM Orders_Details WHERE Orders_id={}".format(oid))
	result = cur.fetchall()
	cur.execute("SELECT TotalAmt FROM Orders WHERE Orders_id={}".format(oid))
	total = cur.fetchone()['TotalAmt']
	return render_template('orderdet.html',rows = result,total = total,oid=oid)

@app.route("/my-orders",methods=['GET'])
def my_orders():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	query = "SELECT * FROM Orders WHERE Cust_id={} ORDER BY Orders_id DESC".format(cid)
	cur.execute(query)
	result = cur.fetchall()
	return render_template('myorders.html',rows = result)

@app.route("/myaccount",methods=['GET'])
def my_account():
	uid = current_user.userid
	type = current_user.type
	if type=='c':query = "SELECT * FROM Customer WHERE Cust_id={}".format(uid)
	else:query = "SELECT * FROM Seller WHERE Seller_id={}".format(uid)
	cur = db.connection.cursor()
	cur.execute(query)
	result = cur.fetchone()
	return render_template('myaccount.html',row = result,uid = uid,type=type)

@app.route("/liked",methods=['GET'])
def liked():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	query = "SELECT * FROM product WHERE Prod_id IN (SELECT Prod_id FROM views WHERE Cust_id={} AND Likes=1)".format(cid)
	cur.execute(query)
	result = cur.fetchall()
	return render_template('liked.html',rows = result)

@app.route("/wallet",methods=['GET'])
def wallet():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	cur = db.connection.cursor()
	wallet=0
	query="SELECT SUM(Amount) AS Balance FROM Wallet WHERE Cust_id={}".format(cid)
	cur.execute(query)
	result = cur.fetchone()
	if result['Balance'] is not None:wallet = result['Balance']
	query = "SELECT * FROM Wallet WHERE Cust_id={} ORDER BY Txn_id DESC".format(cid)
	cur.execute(query)
	result = cur.fetchall()
	return render_template('wallet.html',rows = result,balance = wallet)

@app.route("/wallet/topup",methods=['GET'])
def wallet_topup():
	if current_user.type=='s':return redirect(url_for('seller_home'))
	cid = current_user.userid
	amount = request.args.get('amt')
	query = "INSERT into Wallet(Amount,Type,Tdate,Cust_id) VALUES({},'Cr',curdate(),{})".format(amount,cid)
	cur = db.connection.cursor()
	cur.execute(query)
	db.connection.commit()
	return redirect(url_for("wallet"))

@app.route("/seller/update",methods=['GET'])
def seller_update():
	if current_user.type=='c':return redirect(url_for('home'))
	pid = request.args.get('pid')
	what = request.args.get('what')
	value = int(request.args.get('value'))
	cur = db.connection.cursor()
	if what=='qty':
		cur.execute("SELECT Stock FROM product WHERE Prod_id={}".format(pid))
		old_qty = cur.fetchone()['Stock']
		#value = value + old_qty
		query = "UPDATE Product SET Stock={} WHERE Prod_id={}".format(value,pid)
	if what=='price':
		query = "UPDATE Product SET Price={} WHERE Prod_id={}".format(value,pid)
	if what=='disc':
		query = "UPDATE Product SET Discount={} WHERE Prod_id={}".format(value,pid)
	cur.execute(query)
	db.connection.commit()
	return redirect(url_for("seller_home"))

@app.route("/seller/home",methods=['GET'])
@login_required
def seller_home():
	if current_user.type=='c':return redirect(url_for('home'))
	sid = current_user.userid
	cur = db.connection.cursor()
	query = "SELECT * FROM product WHERE Seller_id={}".format(sid)
	cur.execute(query)
	result = cur.fetchall()
	return render_template('s_home.html',rows = result)

@app.route("/seller/orders",methods=['GET'])
@login_required
def seller_orders():
	if current_user.type=='c':return redirect(url_for('home'))
	sid = current_user.userid
	cur = db.connection.cursor()
	query = "SELECT p.Prod_id as A,p.Name as B,o.Orders_id as C,OrdersDate as D,Quantity as E,Amount as F FROM Orders as o,Orders_Details as od,Product as p WHERE o.Orders_id=od.Orders_id and od.Prod_id=p.Prod_id and Seller_id={} ORDER BY OrdersDate DESC".format(sid)
	cur.execute(query)
	result = cur.fetchall()
	return render_template('s_orders.html',rows = result)

@app.route("/seller/analytics/<what>",methods=['GET'])
@login_required
def seller_analytics(what):
	if current_user.type=='c':return redirect(url_for('home'))
	
	
	todaydate=datetime.now()
	todaydate = str(todaydate).split(" ")[0]+' '+'00:00:00'
	date15=datetime.now() - timedelta(days=14)
	date15 = str(date15).split(" ")[0]+' 00:00:00'
	#print(todaydate,date15)
	sid = current_user.userid
	if what=="qty":
		# os.remove('app/static/sgrapha.png')
		query="SELECT sum(od.Quantity) AS Quantity,o.OrdersDate AS Date FROM Orders AS o JOIN orders_details AS od ON o.Orders_id = od.Orders_id JOIN Product AS p ON od.Prod_id = p.Prod_id WHERE (o.OrdersDate>='"+date15+"' AND o.OrdersDate<='"+todaydate+"') AND p.Seller_id={} GROUP BY Date".format(sid)
		title="Sales Analytics - Quantity"	
		#subprocess.call(["python","app/forecastingq.py"], shell=True)
	else:
		# os.remove('app/static/sgraphq.png')
		query="SELECT sum(od.Amount) AS Amount,o.OrdersDate AS Date FROM Orders AS o JOIN orders_details AS od ON o.Orders_id = od.Orders_id JOIN Product AS p ON od.Prod_id = p.Prod_id WHERE (o.OrdersDate>='"+date15+ "'AND o.OrdersDate<='"+todaydate+"') AND p.Seller_id={} GROUP BY Date".format(sid)
		title="Sales Analytics - Amount"
	subprocess.call(["python","app/sellerforecast.py",query], shell=True)	
	#sforecast(query)
	return render_template('s_analytics.html',title=title)

@app.route("/seller/product-analytics",methods=['GET'])
@login_required
def product_analytics():
	if current_user.type=='c':return redirect(url_for('home'))
	
	todaydate=datetime.now()
	todaydate = str(todaydate).split(" ")[0]+' '+'00:00:00'
	date15=datetime.now() - timedelta(days=14)
	date15 = str(date15).split(" ")[0]+' 00:00:00'

	sid = current_user.userid
	pid = request.args.get('pid')
	what = request.args.get('what')

	if what=="qty":
		query="SELECT sum(od.Quantity) AS Quantity,o.OrdersDate AS Date FROM Orders AS o JOIN orders_details AS od ON o.Orders_id = od.Orders_id JOIN Product AS p ON od.Prod_id = p.Prod_id WHERE (o.OrdersDate>='"+date15+"' AND o.OrdersDate<='"+todaydate+"') AND p.Seller_id={} AND p.Prod_id={} GROUP BY Date".format(sid,pid)
		title="Sales Analytics - Quantity"
	else:
		query="SELECT sum(od.Amount) AS Amount,o.OrdersDate AS Date FROM Orders AS o JOIN orders_details AS od ON o.Orders_id = od.Orders_id JOIN Product AS p ON od.Prod_id = p.Prod_id WHERE (o.OrdersDate>'"+date15+"' AND o.OrdersDate<='"+todaydate+"') AND p.Seller_id={} AND p.Prod_id={} GROUP BY Date".format(sid,pid)
		title="Sales Analytics - Amount"
	cur = db.connection.cursor()
	cur.execute("SELECT Name,Prod_id,Stock FROM Product WHERE Prod_id={}".format(pid))
	result = cur.fetchone()
	subprocess.call(["python","app/sellerforecast.py",query], shell=True)
	return render_template('s_analytics.html',title=title,prod=result)