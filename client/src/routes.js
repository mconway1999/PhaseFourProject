import App from "./components/App";
import AddCoffeeShop from "./components/AddCoffeeShop";
import CouponsList from "./components/CouponsList";
import ReviewsList from "./components/ReviewsList";
import ErrorPage from "./components/ErrorPage";
import AddReview from "./components/AddReview";



const routes = [
    {
        path: "/",
        element: <App/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path:'/',
                element: <ReviewsList/>
            },
            {
                path: "/coupons",
                element: <CouponsList/>
            },
            {
                path: "/addreview",
                element: <AddReview/>
            },
            {
                path: "/addcoffeeshop",
                element: <AddCoffeeShop/>
            }
        ]
    }
]

export default routes;