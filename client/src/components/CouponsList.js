import React, { useEffect, useState } from "react";
import { useOutletContext } from "react-router-dom";
import Coupons from "./Coupons";

function CouponsList() {
        const {coupons} = useOutletContext();
        console.log(coupons)
    
        const couponComponents = coupons.map(coupon => {
            return(<Coupons key = {coupon.id} coupon={coupon}/>)
        })
        return (
            <ul>{couponComponents}</ul>
        )
    
  }

export default CouponsList;