import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom"


function NavBar() {
    return (
        <nav>
        <NavLink to="/">Home</NavLink>
        <br/>
        <NavLink to="/coupons">View Coupons</NavLink>
        <br/>
        <NavLink to="/addreview">Add a Review</NavLink>
        <br/>
        <NavLink to ="/addcoffeeshop">Add a Coffee Shop</NavLink>
    </nav>
    )
  }
  

export default NavBar;