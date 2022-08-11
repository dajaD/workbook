import { render, screen } from "@testing-library/react";
import App from "../App";
import userEvent from "@testing-library/user-event";

test("Order phases for happy path with no toppings", async () => {
  //render app
  render(<App />);

  //add ice cream scoops and toppings
  const vanillaInput = await screen.findByRole("spinbutton", {
    name: "Vanilla",
  });
  userEvent.clear(vanillaInput);
  userEvent.type(vanillaInput, "2");

  const chocaolateInput = await screen.findByRole("spinbutton", {
    name: "Chocolate",
  });
  userEvent.clear(chocaolateInput);
  userEvent.type(chocaolateInput, "2");

  screen.debug();

  //find and click order button
  const orderButton = await screen.findByRole("button", {
    name: /order sundae!/i,
  });
  await userEvent.click(orderButton);

  //   //check summary information based on order
  const summaryHeading = screen.getByRole("heading", {
    name: "Order Summary",
  });
  expect(summaryHeading).toBeInTheDocument();

  const scoopHeading = screen.getByRole("heading", { name: "Scoops: $8.00" });
  expect(scoopHeading).toBeInTheDocument("Scoops: $8.00");

  screen.debug();

  const toppingHeading = screen.queryByRole("heading", { name: /toppings/i });
  screen.debug();
  expect(toppingHeading).not.toBeInTheDocument();
});
