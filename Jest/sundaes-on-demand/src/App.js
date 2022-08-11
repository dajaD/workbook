import { useState } from "react";
import Container from "react-bootstrap/Container";
import { OrderDetailsProvider } from "./contexts/OrderDetails";
import OrderConfirmation from "./pages/confirmation/OrderConfirmation";
import OrderEntry from "./pages/entry/OrderEntry";
import OrderSummary from "./pages/summary/OrderSummary";

{
  /**will  display components conditionally */
}
{
  /**summary and entry page need provider*/
}
{
  /** confirmation page does not need provider */
}
export default function App() {
  // orderPhase expects to be 'inProgress', 'review', or 'completed'
  //initail state is inprogress
  const [orderPhase, setOrderPhase] = useState("inProgress");

  // compondent ----> store which top level page will be displayed
  //changes based on value of order phase
  let Component = OrderEntry; // default to order page
  switch (orderPhase) {
    case "inProgress":
      Component = OrderEntry;
      break;
    case "review":
      Component = OrderSummary;
      break;
    case "completed":
      Component = OrderConfirmation;
      break;
    default:
  }

  return (
    <OrderDetailsProvider>
      <Container>{<Component setOrderPhase={setOrderPhase} />}</Container>
    </OrderDetailsProvider>
  );
}
