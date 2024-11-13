import React, { useEffect, useState } from "react";
import Review from "./Review";
import { useOutletContext } from "react-router-dom";

function ReviewsList() {
        const {reviews} = useOutletContext();
        console.log(reviews)
    
        const reviewComponents = reviews.map(review => {
            return(<Review key = {review.id} review={review}/>)
        })
        return (
            <ul>{reviewComponents}</ul>
        )
  }

export default ReviewsList;