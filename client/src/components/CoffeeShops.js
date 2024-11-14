import React, { useEffect, useState } from "react";

function CoffeeShops({coffeeshop}) {

    console.log(coffeeshop)
    return (
    <li>
       <h1>Coffee Shop # {coffeeshop.id}</h1>
       <h2>Coffee Shop Name: {coffeeshop.name}</h2>
       <img>{coffeeshop.image}</img>
    </li>);
  }
  
export default CoffeeShops;