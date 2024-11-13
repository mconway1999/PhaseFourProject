import React, { useState } from "react";
import { useOutletContext } from "react-router-dom";

function Review({review}) {
    console.log(review)

   const {editReview, deleteReview} = useOutletContext()

    function handleDeleteButtonClick(){
      deleteReview(review.id)
  }
    

    return (
    <li>
        <h2>review # {review.id} </h2>
        <h1>name: {review.customer.name}</h1>
        <h1>coffee shop: {review.coffee_shop.name}</h1>
        <img src = {review.coffee_shop.image}/>
        <h1>review: {review.review}</h1>
        <h1>stars: {review.stars}</h1>
        <button onClick={handleDeleteButtonClick}>Delete Review {review.id}</button>
    </li>);
  }
  


export default Review;