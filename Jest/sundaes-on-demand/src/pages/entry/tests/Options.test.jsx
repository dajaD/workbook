import {
  render,
  screen,
  waitFor,
} from "../../../test-utils/testing-library-utils";
// ^^ allows for the wrapper not needing to be rendered in each test
import userEvent from "@testing-library/user-event";
import Options from "../Options";
import { OrderDetailProvider } from "../../../contexts/OrderDetails";

//whenever ruomg

test("displays image for each scoop option from server", async () => {
  render(<Options optionType="scoops" />);

  //find images
  //query to look for multiple images
  const scoopImages = await screen.findAllByRole("img", {
    name: /scoop$/i,
  });
  //gets the number for the length from the handlers.js
  expect(scoopImages).toHaveLength(2);

  //confirm altTextof images
  //@ts-ignore
  //finds the images
  //needs a 'wait' and 'findby'
  //IMPORTANT!!!!!
  //WHEN WAITING FOR SOMETHING To APPEAR ASYNCHRONOUSLY ON THE PAGE YOU MUST USE 'await' AND  'findby' ---> when there are asynchronous elements appearing on the dom have to wait to find them
  const altText = scoopImages.map((element) => element.alt);
  expect(altText).toEqual(["Chocolate scoop", "Vanilla scoop"]);
});

test("display image for each topping option from server", async () => {
  render(<Options optionType="toppings" />);

  //find images
  //query to look for multiple images
  //async action even if daya is from a service worker
  const toppingImages = await screen.findAllByRole("img", {
    name: /topping$/i,
  });
  expect(toppingImages).toHaveLength(3);
  //confirm altTextof images
  //@ts-ignore
  //finds the images
  //needs a 'wait' and 'findby'

  const altText = toppingImages.map((element) => element.alt);
  expect(altText).toEqual([
    "Cherries topping",
    "M&Ms topping",
    "Hot fudge topping",
  ]);
});

test("checking to make sure the total does not update if the scoops input is invalid ", async () => {
  render(<Options optionType={"scoops"} />);
  //optionTypes only has one prop (scoops)

  //checks for chocolate spin button, and adds an invalid value
  const chocolateInput = await screen.findByRole("spinbutton", {
    name: "Chocolate",
  });
  await userEvent.clear(chocolateInput);
  await userEvent.type(chocolateInput, "-2");
  //checks to make sure the value was actually added
  expect(chocolateInput).toHaveValue(-2);

  //checking to make sure that the subtotal was not updated
  //will not work if the react code is not updated.
  const scoopSubtotal = screen.getByText("Scoops total: $0.00");
  expect(scoopSubtotal).toBeInTheDocument();
  screen.debug();
});
