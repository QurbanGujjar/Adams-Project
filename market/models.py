# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField

from market import app
from market import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma =Marshmallow(app)

#        Model created for user or Admin
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_text_password):
        print(plain_text_password)
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        
    def check_password_correction(self,attempted_password):
        print(attempted_password)
        return bcrypt.check_password_hash(self.password_hash,attempted_password)    

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =User
        
#        Model created for Items or Brands
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Brands = db.Column(db.String(length=50), nullable=False, unique=True)
    grams = db.Column(db.String(length=12), nullable=False)
    Packing = db.Column(db.Integer(), nullable=False)
    Rate = db.Column(db.Float(), nullable=False)
    
    def __repr__(self):
        return f'Item {self.Brands}'
class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =Item 


#        Model created for booker 
class Booker(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    booker_code = db.Column(db.String(length=50), nullable=False, unique=True)
    booker_name = db.Column(db.String(length=12), nullable=False)
    
    def __repr__(self):
        return f'Booker {self.booker_code}'
class BookerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =Booker   
        
#  Model Created for Orders
# console.log(order_NO, bookercode, bookername, totalgrossamount, expenses, totalamount)
class Orders(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Order_no = db.Column(db.String(length=50), nullable=False)
    delivered_date = db.Column(db.String(length=50), nullable=False)
    Booker_code = db.Column(db.String(length=15), nullable=False)
    Booker_name = db.Column(db.String(length=50), nullable=False)
    totalgrossamount=db.Column(db.String(length=50), nullable=False)
    GST=db.Column(db.String(length=50), nullable=False)
    Expenses=db.Column(db.String(length=50), nullable=False)
    Total_amount = db.Column(db.String(length=50), nullable=False)
    Status = db.Column(db.String(length=15), nullable=False)
    
    def __repr__(self):
        return f'Orders {self.id}'
class OrdersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =Orders     
    
    

#  Model Created for Order details 

class Orderdetails(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Order_no = db.Column(db.String(length=50), nullable=False)
    Brand_code = db.Column(db.String(length=15), nullable=False)
    Brand_name = db.Column(db.String(length=50), nullable=False)
    grams = db.Column(db.String(length=12), nullable=False)
    Catan = db.Column(db.String(length=12), nullable=False)
    Piece = db.Column(db.String(length=12), nullable=False)
    Unit_piece = db.Column(db.String(length=12), nullable=False)
    Gross_amount = db.Column(db.String(length=15), nullable=False)
    # Rate = db.Column(db.Float(), nullable=False)
    
    def __repr__(self):
        return f'Orderdetails {self.id}'
class OrderdetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model =Orderdetails      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class Item(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=30), nullable=False, unique=True)
#     price = db.Column(db.Integer(), nullable=False)
#     barcode = db.Column(db.String(length=12), nullable=False, unique=True)
#     description = db.Column(db.String(length=1024), nullable=False, unique=True)
#     owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
#     def __repr__(self):
#         return f'Item {self.name}'    
