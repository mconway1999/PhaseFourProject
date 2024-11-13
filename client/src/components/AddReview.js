import React, { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import CoffeeShopList from "./CoffeeShopList";

function AddReview({review}) {
    const {addReview} = useOutletContext();

    const [formData, setFormData] = useState({
        name : "",
        image: "",
        coffeeshop: "",
        review: "",
        stars: ""
    })

    const {editReview, deleteReview} = useOutletContext()



    function handleSubmit(event){
        event.preventDefault()
        addReview({...formData, stars: Number(formData.stars)})
    }

    function handleDeleteButtonClick(){
        deleteReview(review.id)
    }
    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }



    return (  
    <form onSubmit={handleSubmit}>
    <h1>Add New Review Here!</h1>
    <label htmlFor="name">Name: </label>
    <input onChange={updateFormData} type="text" id="name" name="name" placeholder="New name" value={formData.name} required/>
    <br/><br/>
    <label htmlFor="image">Image: </label>
    <input onChange={updateFormData} type="text" id="image" name="image" placeholder="New image" value={formData.image} required/>
    <br/><br/>
    <label htmlFor="stars">Stars: </label>
    <input onChange={updateFormData} type="number" step="0" id="stars" name="stars" placeholder="New stars" value={formData.stars} required/>
    <br/><br/>
    <label htmlFor="review">Review: </label>
    <input onChange={updateFormData} type="text" id="review" name="review" placeholder="New review" value={formData.review} required/>
    <br/><br/>
    <label htmlFor="coffeeshop">CoffeeShop: </label>
    <input onChange={updateFormData} type="text" id="coffeeshop" name="coffeeshop" placeholder="New coffee shop" value={formData.coffeeshop} required/>
    <br/><br/>
    <input type="submit" value="Add Review"/>
    </form>
)}

export default AddReview;