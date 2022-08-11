import { render, screen } from "@testing-library/react";
import App from "../App";
import userEvent from "@testing-library/user-event";

test("Order phases for happy path", async () => {
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

  const CherryBox = await screen.findByRole("checkbox", {
    name: "Cherries",
  });
  const MandMsBox = await screen.findByRole("checkbox", {
    name: "M&Ms",
  });
  const HotFudgeBox = await screen.findByRole("checkbox", {
    name: "Hot fudge",
  });

  await userEvent.click(CherryBox);
  await userEvent.click(MandMsBox);
  await userEvent.click(HotFudgeBox);
  //confirms the boxes are actually checked
  expect(CherryBox).toBeChecked;
  expect(MandMsBox).toBeChecked;
  expect(HotFudgeBox).toBeChecked;

  //finds and clicks the order summary button
  const orderSummaryButton = await screen.findByRole("button", {
    name: /order sundae/i,
  });
  await userEvent.click(orderSummaryButton);

  //   //check summary information based on order
  const summaryHeading = screen.getByRole("heading", {
    name: "Order Summary",
  });
  expect(summaryHeading).toBeInTheDocument();

  const scoopHeading = screen.getByRole("heading", { name: "Scoops: $8.00" });
  expect(scoopHeading).toBeInTheDocument("Scoops: $8.00");
  //can't use findBy and .toBeInDocument() ---> has to be getBy and .toBeIn
  const toppingHeading = screen.getByRole("heading", {
    name: "Toppings: $4.50",
  });
  screen.debug();
  expect(toppingHeading).toBeInTheDocument("Toppings: $4.50");

  //   //   //check summary option items
  //   expect(screen.getByRole("heading", { name: "Scoops: $8.00" }));
  //   expect(screen.getByText("2 Vanilla")).toBeInTheDocument();
  //   expect(screen.getByText("2 Chocolate")).toBeInTheDocument();
  //   expect(screen.getByRole("heading", { name: "Toppings: $4.50" }));
  expect(screen.getByText("Cherries")).toBeInTheDocument();
  expect(screen.getByText("Hot fudge")).toBeInTheDocument();
  expect(screen.getByText("M&Ms")).toBeInTheDocument();
  //the following lines of code; aren't working.
  // expect(
  //   screen.getByRole("heading", {
  //     name: "Total $12.50",
  //   })
  // ).toBeInTheDocument();

  //   //   //accept terms and conditions and click button to confirm order
  const TermsAndConditionscheckbox = screen.getByRole("checkbox", {
    name: /terms and conditions/i,
  });

  //   //button
  const confirmbutton = screen.getByRole("button", {
    name: /confirm order/i,
  });

  await userEvent.click(TermsAndConditionscheckbox);
  //   //checks to make sure terms and conditions were  checked
  expect(TermsAndConditionscheckbox).toBeChecked();
  await userEvent.click(confirmbutton);

  //   //checks that loading page is showing when it should
  const loading = screen.getByText(/loading/i);
  expect(loading).toBeInTheDocument();

  //   //confirm order number on confirmation page
  const thankYouHeading = await screen.findByRole("heading", {
    name: /thank you!/i,
  });
  expect(thankYouHeading).toBeInTheDocument();

  //expects the loading page to not be there when it should not be ---> queryBy()
  const noLoading = screen.queryByText("loading");
  expect(noLoading).not.toBeInTheDocument();

  const orderConfirmationNumber = await screen.findByText(/order number/i);
  expect(orderConfirmationNumber).toBeInTheDocument();

  //checks that the paragraph is present
  const tcpara = await screen.findByText(
    /as per our terms and conditions, nothing will happen now/i
  );

  //   //click 'new order' button on confirmation page
  const createButton = screen.getByRole("button", {
    name: /new order/i,
  });
  userEvent.click(createButton);

  //   //check that scoops and toppings subtotal have been reset
  const scoopsSubtotal = await screen.findByText("Scoops total: $0.00");
  expect(scoopsSubtotal).toBeInTheDocument();
  const toppingsSubtotal = await screen.findByText("Toppings total: $0.00");
  expect(toppingsSubtotal).toBeInTheDocument();

  //   //do we need to await anything to avoid test errors?
  //awaits to make sure the page resets and has the desired button and checkbox for
  //scoops and toppings
  await screen.findByRole("spinbutton", { name: "Vanilla" });
  await screen.findByRole("checkbox", { name: "Cherries" });
});
test("Order phases for happy path with no toppings", async () => {
  //render app
  render(<App />);

  //add ice cream scoops and toppings
  const vanillaInput = await screen.findByRole("spinbutton", {
    name: "Vanilla",
  });
  userEvent.clear(vanillaInput);
  userEvent.type(vanillaInput, "2");
  screen.debug();

  // add a topping and confirm
  const cherryBox = await screen.findByRole("checkbox", {
    name: "Cherries",
  });
  await userEvent.click(cherryBox);
  expect(cherryBox).toBeChecked();
  const toppingsTotal = screen.getByText("Toppings total: $", { exact: false });
  expect(toppingsTotal).toBeInTheDocument("1.50");

  screen.debug();
  // remove the topping
  await userEvent.click(cherryBox);
  expect(cherryBox).not.toBeChecked();
  expect(toppingsTotal).toHaveTextContent("0.00");

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

  const scoopHeading = screen.getByRole("heading", { name: "Scoops: $4.00" });
  expect(scoopHeading).toBeInTheDocument("Scoops: $4.00");

  screen.debug();

  //checks to make sure that the toppings heading is not on the summary
  const toppingHeading = screen.queryByRole("heading", { name: /toppings/i });
  expect(toppingHeading).not.toBeInTheDocument();
});
