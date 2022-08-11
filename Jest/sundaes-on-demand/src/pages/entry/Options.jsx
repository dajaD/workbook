import axios from "axios";
import ScoopOption from "./ScoopOption";
import ToppingOption from "./ToppingOption";
import Row from "react-bootstrap/Row";
import { useEffect, useState } from "react";
import AlertBanner from "../common/AlertBanner";
import { pricePerItem } from "../../constants";
import { useOrderDetails } from "../../contexts/OrderDetails";
import { formatCurrency } from "../../utilities";
import { act } from "react-dom/test-utils";

// optionType is a dependency array
//this is going to run once on component mount and then it will run again if
//the option type ever changes ---> not likely to happen
//if option is running for scoops, will always run for scoops
export default function Options({ optionType }) {
  const [items, setItems] = useState([]);
  //data will be stored in items ^^ because we can set items to store it in the state

  //store if there is an error in state
  const [error, setError] = useState(false);

  //destructure the value when running orderdetails
  //first is the array [orderDetails]
  const [orderDetails, updateItemCount] = useOrderDetails();

  //optionType is 'scoops' or 'toppings'
  //if the option type prop ever changes, want to rerun this axios call
  act(() => {
    useEffect(() => {
      axios
        .get(`http://localhost:3030/${optionType}`)
        .then((response) => setItems(response.data))
        .catch((error) => setError(true));
    }, [optionType]);
  });
  //returns the alert component with the default props
  //imports alert component
  if (error) {
    //@ts-ignore
    return <AlertBanner />;
  }

  //determine what kind of subcomponent based on whether option type of scoop or toppings

  //TODO: replace 'null' with ToppingOption when available
  //will render a bunch of scoopOptions from the server
  const ItemComponent = optionType === "scoops" ? ScoopOption : ToppingOption;

  //to make the title will take the optionType and capitalize the first letter
  const title = optionType[0].toUpperCase() + optionType.slice(1).toLowerCase();

  //series of subcomponents
  //Scoop's scoop options or tarping option that will display within this component

  //array of components called optionItems
  //changes fron an array of data to an array of components
  //rending an array of item components ----> needs a key
  //pass updateItemCount to child component
  const optionsItems = items.map((item) => (
    <ItemComponent
      key={item.name}
      name={item.name}
      imagePath={item.imagePath}
      updateItemCount={(itemName, newItemCount) =>
        updateItemCount(itemName, newItemCount, optionType)
      }
    />
  ));

  //return fragment => dont need an averarching div for structural reasons
  return (
    <>
      <h2>{title}</h2>
      <p>{formatCurrency(pricePerItem[optionType])} each</p>
      <p>
        {title} total: {orderDetails.totals[optionType]}
      </p>
      <Row>{optionsItems}</Row>
    </>
  );
}
