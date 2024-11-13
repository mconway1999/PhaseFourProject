import React, { useEffect, useState } from "react";
import CoffeeShopList from "./CoffeeShopList";
import { useOutletContext } from "react-router-dom";

function AddCoffeeShop() {
    const {addCoffeeShop} = useOutletContext();

    const [formData, setFormData] = useState({
        name : "",
        image: ""
    })

    function handleSubmit(event){
        event.preventDefault()
        addCoffeeShop({...formData, name: Text(formData.name)})
    }
    function updateFormData(event){
        setFormData({...formData, [event.target.name]: event.target.value})
    }

   
    return( 
    <form onSubmit={handleSubmit}>
    <h1>Add New Coffee Shop Here!</h1>
    <label htmlFor="name">Name: </label>
    <input onChange={updateFormData} type="text" id="name" name="name" placeholder="New name" value={formData.name} required/>
    <br/><br/>
    <label htmlFor="image">Image: </label>
    <input onChange={updateFormData} type="text" id="image" name="image" placeholder="New image" value={formData.image} required/>
    <br/><br/>
    <input type="submit" value="Add Coffee Shop"/>
    </form>
    )}
  

export default AddCoffeeShop;