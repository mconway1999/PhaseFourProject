from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates


from config import db

class CoffeeShop(db.Model, SerializerMixin):
     __tablename__ ='coffee_shops'
     id = db.Column(db.Integer, primary_key=True)
     image = db.Column(db.String, nullable=False)
     name = db.Column(db.String, nullable=False)

     coupons = db.relationship('Coupons', back_populates = 'coffee_shop')
     reviews = db.relationship('Reviews', back_populates = 'coffee_shop')

     @validates('name')
     def validate_review(self, column, value):
        if type(value) == str:
            return value
        else:
            raise Exception(f"{column} must be a string")

class Coupons(db.Model, SerializerMixin):
     __tablename__ ='coupons'
     id = db.Column(db.Integer, primary_key=True)
     coupon_comment = db.Column(db.String, nullable=False)
     coffee_shop_id=db.Column(db.Integer,db.ForeignKey('coffee_shops.id'), nullable=False)
    
     coffee_shop = db.relationship('CoffeeShop', back_populates='coupons')

     @validates('coupon_comment')
     def validate_review(self, column, value):
        if type(value) == str and len(value) >= 10:
            return value
        else:
            raise Exception(f"{column} must be a string and it must be at least 10 characters long")

class Customers(db.Model, SerializerMixin):
     __tablename__ ='customers'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     
     reviews = db.relationship('Reviews', back_populates = 'customer')

     @validates('name')
     def validate_name(self, column, value):
        if type(value) == str:
            return value
        else:
            raise Exception(f"{column} must be a string")

class Reviews(db.Model, SerializerMixin):
     __tablename__ ='reviews'
     id = db.Column(db.Integer, primary_key=True)
     review = db.Column(db.String, nullable=False)
     stars = db.Column(db.Integer, nullable=False)

     customer_id=db.Column(db.Integer, db.ForeignKey('customers.id'))
     coffee_shop_id=db.Column(db.Integer, db.ForeignKey('coffee_shops.id'))

     customer = db.relationship('Customers', back_populates="reviews")
     coffee_shop = db.relationship('CoffeeShop', back_populates="reviews")


     @validates('review')
     def validate_review(self, column, value):
        if type(value) == str and len(value) >= 8:
            return value
        else:
            raise Exception(f"{column} must be a string and it must be at least 8 characters long")
        
     @validates('stars')
     def validate_stars(self, column, value):
        if type(value) == int and 1 <= value <= 5:
            return value
        raise Exception(f"{column} must be an integer between 1 and 5")
     

