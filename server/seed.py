#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
from models import db, CoffeeShop, Coupons, Customers, Reviews

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    #fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        coffeeshop1=CoffeeShop(id= 1, name='Java Stop',image='/images/Java_Stop.png')
        coffeeshop2=CoffeeShop(id= 2, name='Esspresso Experience',image='/images/Esspresso_Experience.png')
        coffeeshop3=CoffeeShop(id= 3, name='Sugar Cubes',image='images/Sugar_Cubes.png')
        coffeeshop4=CoffeeShop(id= 4, name='Coffee Craze',image='images/Coffee_Craze.png')
        
        review1 = Reviews (id=1, customer_id=1, coffee_shop_id=1,review='My mobile order was easily submitted and a tasty drink was ready upon my arrival. Perfect experience.', stars=5)
        review2 = Reviews (id=2, customer_id=2, coffee_shop_id=1,review='Great coffee. Croissant was delicious. The shop is a little small, but still 	welcoming and clean.', stars=4)
        review3 = Reviews (id=3,customer_id=3, coffee_shop_id=1, review='best coffee and nicest staff! I couldnt recommend it enough', stars=5)
        review4= Reviews(id=4,customer_id=2, coffee_shop_id=2, review='I was expecting a little more flavour from the roast.', stars=2)
        review5 = Reviews (id=5,customer_id=1, coffee_shop_id=2, review='My new cup started to majorly leak 30 minutes in.', stars=1)
        review6= Reviews (id=6,customer_id=3, coffee_shop_id=2, review='For starters my latte was way too foamy. The espresso was over 	extracted and tasted a bit burnt. I probably wont try again.',stars=1)
        review7= Reviews (id=7, customer_id=2, coffee_shop_id=3, review='Delicious beverages and awesome a service!', stars=5)
        review8= Reviews(id=8,customer_id=1, coffee_shop_id=3, review='Service is passable, decor is neat and cozy, but not a lot of space to sit down and work.', stars=3)
        review9= Reviews(id=9,customer_id=3, coffee_shop_id=3,review='The latte tasted like milk and I had to ask for another shot of espresso.', stars=2)
        review10= Reviews(id=10, customer_id=3, coffee_shop_id=4,review='Pleasant and prompt service. Easy to find on a map. Will be back if Im in the area.', stars=4)
        review11= Reviews(id=11, customer_id=2, coffee_shop_id=4,review='The fact that theyre a smaller chain and try harder with their coffee is 	appreciated.', stars=4)
        review12 = Reviews(id=12, customer_id=1, coffee_shop_id=4,review='5 stars The employees are all friendly and efficient, keeps the line moving fast.', stars=5)
        review13 = Reviews(id=13, customer_id=4, coffee_shop_id=1, review = 'Coffee was okay, employees were plesant', stars = 4)
        review14 = Reviews(id=14, customer_id=4, coffee_shop_id=2, review ='Excellent! I can see why this shop is so popular', stars = 5)
        review15 = Reviews(id=15, customer_id=4, coffee_shop_id=3, review ='Coffee tasted burnt. Did not enjoy', stars = 1 )
        review16 = Reviews(id=16, customer_id=4, coffee_shop_id=4, review = 'Staff was very friendly, coffee was a bit too strong for my taste', stars = 3)

        customer1 = Customers (id=1, name='Stephan')
        customer2 = Customers (id=2, name='Dylan')
        customer3 = Customers (id=3, name='Megan')
        customer4 = Customers (id=4, name='Lisa')

        coupon1 = Coupons (id=1,coffee_shop_id= 1,coupon_comment = '10 percent off!')
        coupon2 = Coupons (id=2,coffee_shop_id= 2,coupon_comment ='20 percent off an order over 25 dollars!')
        coupon3 = Coupons (id=3, coffee_shop_id= 3,coupon_comment = '15 percent off an order over 15 dollars!')
        coupon4 = Coupons (id=4, coffee_shop_id= 4,coupon_comment = '5 dollars off!')
        coupon5 = Coupons (id=5, coffee_shop_id= 1,coupon_comment = '15 percent off for students!')
        coupon6 = Coupons (id=6, coffee_shop_id= 2,coupon_comment = 'buy 2 get one free!')
        coupon7 = Coupons (id=7, coffee_shop_id= 3,coupon_comment = '15 percent off for three or more coffees!')
        coupon8 = Coupons (id=8, coffee_shop_id= 4,coupon_comment = 'BOGO: buy two get one coffee free!')
        coupon9 = Coupons (id=9, coffee_shop_id= 1,coupon_comment = 'BOGO: buy one get a small coffee free!')
        coupon10 = Coupons (id=10, coffee_shop_id= 2,coupon_comment = '15 percent off for seniors!')
        coupon11 = Coupons (id=11, coffee_shop_id= 3,coupon_comment = '20 percent off for four coffees!')
        coupon12 = Coupons (id=12, coffee_shop_id= 4,coupon_comment = 'buy 3 get one free!')


        db.session.add_all([coffeeshop1, coffeeshop2,coffeeshop3,coffeeshop4])
        db.session.add.all([coupon1,coupon2,coupon3,coupon4,coupon5,coupon6,coupon7,coupon8,coupon9,coupon10,coupon11,coupon12])
        db.session.add.all([review1,review2,review3,review4,review5,review6,review7,review8,review9,review10,review11,review12,review13,review14,review16])
        db.session.add.all([customer1,customer2,customer3,customer4])
        db.session.commit()
