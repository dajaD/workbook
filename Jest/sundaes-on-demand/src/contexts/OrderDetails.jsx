import { createContext, useContext, useState, useMemo, useEffect } from "react";
import { pricePerItem } from "../constants";
import { formatCurrency } from "../utilities";

// //function that will format the currency to solve the error:  FAIL  src/pages/entry/tests/totalUpdates.test.jsx
// //  × update scoop subtotal when scoops change (69 ms)
// //  ● update scoop subtotal when scoops change
// // TestingLibraryElementError: Unable to find an element with the text: Scoops total: $.
// //This could be because the text is broken up by multiple elements. In this case, you can provide a
// //function for your text matcher to make your matcher more flexible.
// function formatCurrency(amount) {
//   //intl: international number format -> javascript builtin function

//   return new Intl.NumberFormat("en-US", {
//     style: "currency",
//     currency: "USD",
//     minimumFractionDigits: 2,
//   }).format(amount);
// }

//@ts-ignore
const OrderDetails = createContext();

//custom hook to check whether we're inside a provider
//exporting to be accessible
export function useOrderDetails() {
  const context = useContext(OrderDetails);

  if (!context) {
    throw new Error(
      "useOrderDetails must be used within an OrderDetailsProvider"
    );
  }

  return context;
}

//function to calculate the subtotal
function calculateSubtotal(optionType, optionCounts) {
  //store running count in variable
  let optionCount = 0;
  //runs through the values of the map
  //access the value for that key (optionType) which will give the map and the ability to use the value
  //values() method will go through all of the value

  for (const count of optionCounts[optionType].values()) {
    //update optionCount by the value of 'count'
    //i.e. vanilla map option has a value of 1, chocolate has a value of 2
    //so optionCount would start at 0, then add the 1, and then add the 2, giving a total of 3
    optionCount += count;
  }
  //calculate the subtotal by knowing the price per option
  //created variable constants that hold the scoops at $2, and toppings at $1.5
  //returns the value of option count and the price per option type
  return optionCount * pricePerItem[optionType];
}

//functional component and it will be returing the provider from the context from orderDetails
//exporting to be accessible
export function OrderDetailsProvider(props) {
  //internal state for provider
  //useStstae going to be an objext, default state and will have key of scoops and key of toppings
  //will be a map ===> easier to iterate over just the values, which is going to make
  //it easier to find subtotal
  const [optionCounts, setOptionCounts] = useState({
    scoops: new Map(),
    toppings: new Map(),
  });

  //function that convers the currency being called to create constant zero
  const zeroCurrency = formatCurrency(0);

  const [totals, setTotals] = useState({
    scoops: zeroCurrency,
    toppings: zeroCurrency,
    grandTotal: zeroCurrency,
  });

  //update the totals when the option updates
  //takes a function and dependency array(optionCounts)
  //when optionCOunts changes will run this useEffect to update the total
  useEffect(() => {
    //calculate the subtotal for scoops and toppings
    //need optionCounts because calculateSubtotal will ne ran outside the order details provider
    const scoopsSubtotal = calculateSubtotal("scoops", optionCounts);
    const toppingsSubtotal = calculateSubtotal("toppings", optionCounts);
    const grandTotal = scoopsSubtotal + toppingsSubtotal;
    //make sure the currency is changed to match expected output using formatCurrency function
    setTotals({
      scoops: formatCurrency(scoopsSubtotal),
      toppings: formatCurrency(toppingsSubtotal),
      grandTotal: formatCurrency(grandTotal),
    });
  }, [optionCounts]);

  const value = useMemo(() => {
    //updates context
    function updateItemCount(itemName, newItemCount, optionType) {
      //new copy of option counts
      //which will change using setOptionCounts
      const newOptionCounts = { ...optionCounts };

      //update option count for this item with the new value
      const optionCountsMap = optionCounts[optionType];
      //updated option count has new item count
      optionCountsMap.set(itemName, parseInt(newItemCount));

      //set the state to have the new information from optionCount
      setOptionCounts(newOptionCounts);
    }
    //getter: object containing otpions counts for scoops and toppings, subtotals and totals
    //setter: updateOptionCount => calculate the subtotal and totals whenever the option count changes
    //can get optionCounts for scoops and toppings by spreading

    //array of items being returned
    //updateItemCount is an item being returned so that the component can use this to interact with
    //with the embedded state in the context
    //returns total so that we can access and display them in appropiate components
    return [{ ...optionCounts, totals }, updateItemCount];
    //^^ makes new object with scoops and the value of scoops for optioncounts and toppings
    //^^ and the value of toppings for option counts
  }, [optionCounts, totals]);
  return <OrderDetails.Provider value={value} {...props} />;
}

//exporting orderdetailprovider and useorderdetails
// export { OrderDetailsProvider, useOrderDetails };
