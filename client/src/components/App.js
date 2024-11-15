import React, { useEffect, useState } from "react";
import {Outlet, useNavigate} from "react-router-dom"
import NavBar from "./NavBar";



function App() {

  const [coffeeShops, setCoffeeShops] = useState([]); 
  const [customers, setCustomers] = useState([]);
  const [reviews, setReviews] = useState ([]);
  const [coupons, setCoupons] = useState([]);
  
 

  const navigate = useNavigate()

  useEffect (getCoffeeShops,[])
  useEffect (getCoupons,[])
  useEffect (getReviews,[])
  useEffect (getCustomers,[])

    function getCoffeeShops(){
      fetch('/coffeeshops')
    .then(response => response.json())
    .then(coffeeShopData => setCoffeeShops(coffeeShopData))
    }
    
    function addCoffeeShop(newCoffeeShop){
      fetch('/coffeeshops', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(newCoffeeShop)
      })
      .then(response => {
        if(response.ok){
          response.json().then(newCoffeeShopData => {
            setCoffeeShops([...coffeeShops, newCoffeeShopData])
            navigate('/')
          })
        }
        else{
          response.json().then(errorData => alert(`Error: ${errorData.error}`))
        }
      })
    }
    function getCustomers(){
      fetch('/customers')
      .then(response => response.json())
      .then(customerData => setCustomers(customerData))
    }
    function getReviews(){
      fetch('/reviews')
      .then(response => response.json())
      .then(reviewData => setReviews(reviewData))
    }
    function addReview(newReview){
      fetch('/reviews', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(newReview)
      })
      .then(response => {
        if(response.ok){
          response.json().then(newReviewData => {
            setReviews([...reviews, newReviewData])
            navigate('/')
          })
        }
        else{
          response.json().then(errorData => alert(`Error: ${errorData.error}`))
        }
      })
    }
    function deleteReview(id){
      fetch(`/reviews/${id}`, {
        method: "DELETE"
      })
      .then(response => {
        if(response.ok){
          const updatedReviewArray = reviews.filter(review => {
            return review.id !== id
          })
          setReviews(updatedReviewArray)
        }
      })
    }
    function editReview(id,reviewDataForUpdate){
      fetch(`/reviews/${id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(reviewDataForUpdate)
      })
      .then(response => {
        if(response.ok){
          response.json().then(updatedReview => {
            const updatedReviewArray = reviews.map(review => {
              if(review.id === updatedReview.id){
                return updatedReview
              }
              else{
                return review
              }
            })
            setReviews(updatedReviewArray)
          })
        }
        else{
          response.json().then(errorData => alert(`Error: ${errorData.error}`))
        }
      })
    }
    function getCoupons(){
      fetch('/coupons')
      .then(response => response.json())
      .then(couponData => setCoupons(couponData))
    }
    
    
  return (
  <div>
  <NavBar/>
  <Outlet context={
        {
          reviews: reviews,
          addReview: addReview,
          editReview: editReview,
          deleteReview: deleteReview,
          customers: customers,
          coupons: coupons,
          coffeeShops:coffeeShops,
          addCoffeeShop:addCoffeeShop
        }
      }/>
  </div>)
}


export default App;
