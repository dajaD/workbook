import Button from "react-bootstrap/Button";
import Options from "./Options";
import { useOrderDetails } from "../../contexts/OrderDetails";

//set order phase is a prop
export default function OrderEntry({ setOrderPhase }) {
  const [orderDetails] = useOrderDetails();

  //boolean disables the order button if there aren't any scoops in the order
  //will be an attribute for the button
  //if the scoops total is zero, button enabled if the scoop total is not zero,  enabed.
  const hasNoScoops = orderDetails.totals.scoops === "$0.00";

  return (
    <div>
      <h1>Design Your Sundae!</h1>
      <Options optionType="scoops" />
      <Options optionType="toppings" />
      <h2>Grand total: {orderDetails.totals.grandTotal}</h2>
      <Button disabled={hasNoScoops} onClick={() => setOrderPhase("review")}>
        Order Sundae!
      </Button>
    </div>
  );
}

//components can have functions as props
//i.e.: updateItemCount in scoop/topping option component
//typescript requires prop validators
