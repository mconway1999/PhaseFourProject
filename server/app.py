#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, request
# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']
db.init_app(app) 
api = Api(app)
# Local imports
from config import app, db, api
# Add your model imports
from models import CoffeeShop, Reviews, Customers, Coupons

# Views go here!
class Reviews:
    def post(self):
        review_data = request.json.get('review')
        stars_data = request.json.get('stars')
        try:
            new_review = Reviews(stars=stars_data, review=review_data)
            db.session.add(new_review)
            db.session.commit()
            response_body = new_review.to_dict(only=('id', 'stars', 'review'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "please enter a valid review!"
             }
            return make_response(response_body, 422)
    api.add_resource()

    def patch(self):
        review= db.session.get(Reviews)
        if review:
                for attr in request.json:
                    setattr(review, attr, request.json.get(attr))
                db.session.commit()
                response_body = review.to_dict(only=('review', 'stars', 'id'))
                return make_response(response_body, 200)
        else:
                response_body = {
                    "error": "Please write a valid review!"
                }
                return make_response(response_body, 422)
    api.add_resource()
        
    def delete(self):
        review= db.session.get(Reviews)
        if review:
            db.session.delete(review)
            db.session.commit()
            return make_response({}, 204)
        
        else:
            response_body = {
                "error": "Unable to delete review"
            }
            return make_response(response_body, 404)
    api.add_resource()

class Coupons:
     def get(self):
        coupons = Coupons.query.all()
        response_body = [coupon.to_dict(only=('id', 'coupon_comment')) for coupon in coupons]
        return make_response(response_body, 200)
     api.add_resource()


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

