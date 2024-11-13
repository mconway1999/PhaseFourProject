import React, { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import CoffeeShop from "./CoffeeShops";

function CoffeeShopList() {
   
    const {coffeeshop} = useOutletContext();
    
    const coffeeShopComponents = coffeeshop.map(coffeeshop => {
        return(<CoffeeShop Key = {coffeeshop} />)
    })
    return (
        <ul>{coffeeShopComponents}</ul>
    )
  }
  
export default CoffeeShopList;