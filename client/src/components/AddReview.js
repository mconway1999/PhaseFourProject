import React, { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import CoffeeShopList from "./CoffeeShopList";

function AddReview() {
    const {addReview, editReview} = useOutletContext();

    const [formData, setFormData] = useState({
        name : "",
        image: "",
        coffeeshop: "",
        review: "",
        stars: "",
        customer_id:1,
        coffee_shop_id:1
    })


    // function handleUpdateStars(event){
    //         event.preventDefault()
    //         addReview({...formData, stars: Number(formData.stars)})
    // }

    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }


    function handleSubmit(event){
        event.preventDefault()
        addReview({...formData, stars : parseInt(formData.stars)})
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
    <select onChange={updateFormData} name="stars" htmlFor="stars">
    <option value="">--Stars--</option>
    <option value="1">one star</option>
    <option value="2">two stars</option>
    <option value="3">three stars</option>
    <option value="4">four stars</option>
    <option value="5">five stars</option>
    </select>
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