import Options from "./Options";
import {
  OrderDetailsProvider,
  useOrderDetails,
} from "../../contexts/OrderDetails";

export default function OrderEntry() {
  const [orderDetails] = useOrderDetails();
  return (
    <div>
      <Options optionType="scoops" />
      <Options optionType="toppings" />
      <h2>Grand total: {orderDetails.totals.grandTotal} </h2>
    </div>
  );
}
