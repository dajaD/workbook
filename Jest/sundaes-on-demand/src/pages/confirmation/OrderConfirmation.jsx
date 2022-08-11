import React, { useEffect, useState } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import { useOrderDetails } from "../../contexts/OrderDetails";
import AlertBanner from "../common/AlertBanner";

//gets a set orderphase setter that comes from app component
//help move to the next phase when button is pressed
export default function OrderConfirmation({ setOrderPhase }) {
  //will ignore the first two items in the array from order details ---> destrcting resetOrder
  const [, , resetOrder] = useOrderDetails();
  //sets ordernumber to nll, will help with if statement
  const [orderNumber, setOrderNumber] = useState(null);
  const [error, setError] = useState(false);

  //has no dependcy array --> it will only run once on the component mount
  //this allows for order nmber to not be false
  useEffect(() => {
    axios
      //in real app order details come from context and send with post
      //will post to this order end point
      .post(`http://localhost:3030/order`)
      //techncally doesnt work since the app doesnt work
      .then((response) => {
        //once receives response, set response to order number
        setOrderNumber(response.data.orderNumber);
      })
      .catch((error) => setError(true));
  }, []);

  if (error) {
    //@ts-ignore
    return <AlertBanner message={null/>;
  }

  function handleClick() {
    //clear order details
    resetOrder();

    //send back to order enttry page
    //need to make sure the scoops/toppings clear out
    setOrderPhase("inProgress");
  }

  //if order number is not null, return order confirmation page from mockups
  if (orderNumber) {
    return (
      <div style={{ textAlign: "center" }}>
        <h1>Thank You!</h1>
        <p>Your order number is {orderNumber}</p>
        <p style={{ fontSize: "25%" }}>
          as per our terms and conditions, nothing will happen now
        </p>
        <Button onClick={handleClick}>Create new order</Button>
      </div>
    );
    //if order number is false (null), going to return div that says loading
  } else {
    return <div>Loading</div>;
  }
}
