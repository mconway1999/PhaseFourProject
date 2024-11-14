#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, request
# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate
from config import app, db, api
import ipdb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] 


# Local imports


# Add your model imports
from models import CoffeeShop, Reviews, Customers, Coupons

# Views go here!
class AllReviews(Resource):
    def get(self):
        reviews = Reviews.query.all()
        response_body = [review.to_dict(only=('id', 'stars', 'review', 'customer.name','coffee_shop.name', 'coffee_shop.image')) for review in reviews]
        return make_response(response_body, 200)
    def post(self):
        review_data = request.json.get('review')
        stars_data = request.json.get('stars')
        customer_id_data = request.json.get('customer_id')
        coffee_shop_id_data = request.json.get('coffee_shop_id')
       
        try:
            new_review = Reviews(stars=stars_data, review=review_data, customer_id=customer_id_data,coffee_shop_id=coffee_shop_id_data)
            db.session.add(new_review)
            db.session.commit()
            response_body = new_review.to_dict(only=('id', 'stars', 'review','customer.name','coffee_shop.name', 'coffee_shop.image'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "please enter a valid review!"
             }
            return make_response(response_body, 422)
api.add_resource(AllReviews, '/reviews')


class ReviewByID(Resource):
    def patch(self,id):
        review= db.session.get(Reviews,id)
        if review:
                for attr in request.json:
                    setattr(review, attr, request.json.get(attr))
                db.session.commit()
                response_body = review.to_dict(only=('review', 'stars', 'id','customer.name','coffee_shop.name', 'coffee_shop.image'))
                return make_response(response_body, 200)
        else:
                response_body = {
                    "error": "Please write a valid review!"
                }
                return make_response(response_body, 422)

    def delete(self,id):
        review= db.session.get(Reviews,id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return make_response({}, 204)
        
        else:
            response_body = {
                "error": "Unable to delete review"
            }
            return make_response(response_body, 404)
api.add_resource(ReviewByID, '/reviews/<int:id>')

class AllCoupons(Resource):
     def get(self):
        coupons = Coupons.query.all()
        response_body = [coupon.to_dict(only=('id', 'coupon_comment','coffee_shop.name')) for coupon in coupons]
        return make_response(response_body, 200)
     def post(self):
        coupon_comment_data = request.json.get('coupon_comment')
        coffee_shop_name_data = request.json.get ('coffee_shop_name')
        try:
            new_coupon = Coupons(coupon_comment=coupon_comment_data, coffee_shop_name = coffee_shop_name_data)
            db.session.add(new_coupon)
            db.session.commit()
            response_body = new_coupon.to_dict(only=('id', 'coupon_comment', 'coffee_shop.name'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "please enter a valid coupon!"
             }
            return make_response(response_body, 422)
api.add_resource(AllCoupons, '/coupons')


class AllCustomers(Resource):
    def get(self):
        customers = Customers.query.all()
        response_body = [customer.to_dict(only=('id', 'name')) for customer in customers]
        return make_response(response_body, 200)
    

    def post(self):
        name_data = request.json.get('name')
        try:
            new_customer = Customers(name=name_data)
            db.session.add(new_customer)
            db.session.commit()
            response_body = new_customer.to_dict(only=('id', 'name'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "please enter a valid customer!"
             }
            return make_response(response_body, 422)
api.add_resource(AllCustomers, '/customers')

class AllCoffeeShops(Resource):
     def get(self):
        coffeeshops = CoffeeShop.query.all()
        response_body = [coffeeshop.to_dict(only=('id', 'image', 'name')) for coffeeshop in coffeeshops]
        return make_response(response_body, 200)
     
     def post(self):
        name_data = request.json.get('name')
        image_data = request.json.get('image')
        try:
            new_coffee_shop = CoffeeShop(image=image_data, name=name_data)
            db.session.add(new_coffee_shop)
            db.session.commit()
            response_body = new_coffee_shop.to_dict(only=('id', 'image', 'name'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "please enter a valid coffee shop!"
             }
            return make_response(response_body, 422)
api.add_resource(AllCoffeeShops, '/coffeeshops')




@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

