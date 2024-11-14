import React, { useState } from "react";
import { useOutletContext } from "react-router-dom";

function Review({review}) {
    
  const [stars, setStars] = useState({
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5
  });

   const {deleteReview, editReview} = useOutletContext()

    function handleDeleteButtonClick(){
      deleteReview(review.id)
  }
    function handleUpdateStars(event){
      event.preventDefault()
      Review(editReview(stars))
    }


    return (
    <li>
        <h2>review # {review.id} </h2>
        <h1>name: {review.customer.name}</h1>
        <h1>coffee shop: {review.coffee_shop.name}</h1>
        <img src = {review.coffee_shop.image}/>
        <h1>review: {review.review}</h1>
        <select onChange={handleUpdateStars} name="stars" htmlFor="stars">
          <option value = "1">One Star </option>
          <option value = "2">Two Stars </option>
          <option value = "3">Three Stars </option>
          <option value = "4">Four Stars </option>
          <option value = "5">Five Stars </option>
        </select>
        <button onClick={handleDeleteButtonClick}>Delete Review {review.id}</button>
    </li>);
  }
  


export default Review;