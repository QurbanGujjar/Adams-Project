from numpy import integer
from market import app
from flask import flash,render_template,request,redirect,jsonify,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
from market.form import RegisterForm,LoginForm,BookerForm
from flask_login import login_user
from market.models import Item, Orderdetails,OrderdetailsSchema,User,db,UserSchema,ItemSchema,Booker,BookerSchema,Orders
# from market import db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MumtazBrothers.db'

# Mumtaz Brothers
@app.template_filter("clean_date")
def clean_date(dt):
  return dt.strftime("%d %b %Y")


@app.route("/")
@app.route("/home")
def home():
  return render_template("/home.html")
  
  
@app.route("/dashboard")
def dashboard():
  return render_template("/dashboard.html")  

@app.route('/items')
def market_page():
  items=Item.query.all()
  return render_template("/market.html",items=items)


@app.route('/order_list')
def order_list():
  items=Orders.query.all()
  return render_template("/order_list.html",items=items)


@app.route('/bookers')
def bookers_page():
  my_booker=Booker.query.all()
  return render_template("/Booker.html",my_booker=my_booker)


@app.route("/order")
def order_page():
  form= BookerForm()  
  sql=text('SELECT Order_no FROM orders ORDER BY id DESC LIMIT 1')
  result = db.engine.execute(sql)
  last_order_id=0
  for row in result:
      last_order_id=row[0]
  x = int(last_order_id.split("_")[1])+1
  nextorder="SN_"+str(x)    
  return render_template("/order.html",form=form,order_NO=nextorder)


@app.route("/Edit-Order/<Order_no>")
def edit_order(Order_no):
  form= BookerForm()
  print(Order_no)
  items=Orderdetails.query.filter_by(Order_no=Order_no).all()
  return render_template("/order.html",form=form,order_NO=Order_no,items=items)


@app.route('/getbookers',methods=['GET','POST'])
def getbookers():
  if request.method == 'POST':
    form = request.form
    booker_name=form['ID']
    booker_name =booker_name+"%"  
    sql = text(f'select * from booker where booker_name like"{booker_name}"')
    booker = db.engine.execute(sql)
    Booker_Schema=BookerSchema(many=True)
    bookers=Booker_Schema.dump(booker)
    print(bookers)
    return jsonify({'bookers': bookers})
  return render_template("/market.html")



@app.route('/getbooker',methods=['GET','POST'])
def getbooker():
  if request.method == 'POST':
    form = request.form
    bookerID=form['ID']
    booker=Booker.query.filter_by(id=bookerID).first()
    print(booker)
    Booker_Schema=BookerSchema()
    bookers=Booker_Schema.dump(booker)
    print(bookers)
    return jsonify({'bookers': bookers})
    
    
    
@app.route('/getbrands',methods=['GET','POST'])
def getbrands():
  if request.method == 'POST':
    form = request.form
    brand=form['ID']
    brand =brand+"%"
    sql = text(f'select * from item where Brands like"{brand}"')
    items = db.engine.execute(sql)
    Item_Schema=ItemSchema(many=True)
    brands=Item_Schema.dump(items)
    # print(items)
    return jsonify({'brands': brands})
  return render_template("/market.html")    



@app.route('/getbrand',methods=['GET','POST'])
def getbrand():
  if request.method == 'POST':
    form = request.form
    bookerID=form['ID']
    items=Item.query.filter_by(id=bookerID).first()
    print(items)
    Item_Schema=ItemSchema()
    items=Item_Schema.dump(items)
    print(items)
    return jsonify({'items': items})
   
    
#    insert order details function:
@app.route("/insert-order-details",methods=['GET','POST'])
def  insert_order_details():
  if request.method=='POST':
    form = request.form
    order_no=form['order_NO']
    print("insert_order_details"+form['order_NO'])
    insert_order=Orderdetails(Order_no=form['order_NO'],Brand_code=form['brandcode'],Brand_name=form['brandname'],
                              grams=form['brandname'],Catan=form['brandCT'],Piece=form['brandPC'],Unit_piece=form['brandrate'],Gross_amount=form['price'])
    
    db.session.add(insert_order)
    db.session.commit()
    
    sql = text(f'select * from orderdetails where Order_no="{order_no}"')
    order_details = db.engine.execute(sql)
    Orderdetails_Schema=OrderdetailsSchema(many=True)
    order_details=Orderdetails_Schema.dump(order_details)
    return jsonify({'order_details': order_details})
   
   
@app.route("/delete-from-orderdetals",methods=['GET','POST'])
def  delete_from_orderdetals():
  if request.method=='POST':
    form = request.form
    id=form['order_id']
    print("id is = ",id)
    ord=Orderdetails.query.filter_by(id=id).first()
    instence=ord.Order_no
   
    Orderdetails.query.filter_by(id=id).delete()
    db.session.commit()
    
    sql = text(f'select * from orderdetails where Order_no="{instence}"')
    order_details = db.engine.execute(sql)
    Orderdetails_Schema=OrderdetailsSchema(many=True)
    order_details=Orderdetails_Schema.dump(order_details)
    return jsonify({'order_details': order_details})
    
    # Save order 
@app.route("/save-new-order",methods=['GET','POST'])
def save_new_order():
  if request.method=='POST':
    form = request.form
    order_no=form['order_NO']
    items=Orders.query.filter_by(Order_no=order_no).first()
    if items:
      items.delivered_date="Date"
      items.Booker_code=form['bookercode']
      items.Booker_name= form['bookername']
      items.totalgrossamount= form['totalgrossamount']
      items.Expenses= form['expenses']
      items.GST=form['GST']
      items.Total_amount= form['totalamount']
      items.Status='OPEN'
      db.session.commit() 
      
      
    else:  
    
      save_order=Orders( Order_no= form['order_NO'],
                        delivered_date="Date",
                        Booker_code=form['bookercode'],
                        Booker_name= form['bookername'],
                        totalgrossamount= form['totalgrossamount'],
                        Expenses= form['expenses'],
                        GST=form['GST'],
                        Total_amount= form['totalamount'],
                        Status='OPEN')
      db.session.add(save_order)
      db.session.commit() 
     
      
  
  return jsonify({'save_order':'Saved'})
  
       
@app.route("/total-gross-ammount",methods=['GET','POST'])
def total_gross_ammount():
  #  if request.method=='POST':
    total_gross=[]
    i=0
    sum=0
    # form = request.form
    order_NO="SN_1"
    # order_NO=form['order_NO']
    respectedorder=Orderdetails.query.filter_by(Order_no=order_NO).all()
    for amout in respectedorder:
       total_gross.append(amout.Gross_amount)
      #  sum=sum+integer(total_gross[i])
      #  i=i+1
      #  integer
    total_gross  
    print(total_gross[1])   
      
    print(respectedorder[1])
    return render_template('/test.html',respectedorder=respectedorder ,total_gross=total_gross)
    
    


@app.route("/register",methods=['GET','POST'])
def register_page():
  form= RegisterForm()
  if form.validate_on_submit():
    user_to_create=User(username=form.username.data,
                        email_address=form.email_address.data,
                        password=form.password1.data)
    db.session.add(user_to_create)
    db.session.commit()
    return redirect(url_for('market_page'))
  if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger') 
  return render_template('register.html',form=form)

@app.route("/login",methods=['GET','POST'])
def login_page():
  form= LoginForm()
  if form.validate_on_submit():
    print(form.username.data)
    print(form.password.data)
    attempted_user=User.query.filter_by(username=form.username.data).first()
    print(attempted_user)
    if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
      # login_user(attempted_user)  
      flash(f"Success ! Your are loged in" )
      return redirect(url_for('market_page'))
  return render_template("/login.html",form=form) 