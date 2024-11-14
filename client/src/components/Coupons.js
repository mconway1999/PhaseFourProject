import React, { useEffect, useState } from "react";

function Coupons({coupon}) {
    return(
    <li>
        <h1>View Coupons Here!</h1>
        <h2>Coupon # {coupon.id}</h2>
        <h2>{coupon.coupon_comment}</h2>
        <h2>{coupon.coffee_shop.name}</h2>
    </li>
    ) 
  }

export default Coupons;