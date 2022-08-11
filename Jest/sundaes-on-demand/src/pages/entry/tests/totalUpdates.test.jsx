import { render, screen } from "../../../test-utils/testing-library-utils";
// import { fireEvent } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Options from "../Options";
import OrderEntry from "../OrderEntry";

test("update scoop subtotal when scoops change", async () => {
  //need to wrap the render and give it component to solve the error:  useOrderDetails must be used within an OrderDetailsProvider
  render(<Options optionType={"scoops"} />);

  //make sure total starts out at 0.00
  //have to use exact false, to make finding the element seperate from my assertion
  //will be reusing as it changes throughout the test
  const scoopsSubtotal = screen.getByText("Scoops total: $", { exact: false });
  expect(scoopsSubtotal).toHaveTextContent("0.00");

  //updates vanilla scoops to 1 and check the subtotal
  const vanillaInput = await screen.findByRole("spinbutton", {
    name: "Vanilla",
  });

  //clears vanilla input
  userEvent.clear(vanillaInput);
  //changes the value for input by inputting text
  await userEvent.type(vanillaInput, "1");
  //^^ this line of code does not work for some reason => needs await to work properly
  // fireEvent.change(vanillaInput, {
  //   target: { value: "1" },
  // });

  // expect(screen.getByText("OPTION1")).toBeInTheDocument();
  //checks to see what the subtotal is after vanilla scoop
  //===== test currently gets caught here
  expect(scoopsSubtotal).toHaveTextContent("2.00");

  //updates chocolate scoops to 2 and check the subtotal
  const chocolateInput = await screen.findByRole("spinbutton", {
    name: "Chocolate",
  });
  //clears chocolate input
  userEvent.clear(chocolateInput);
  //changes the value for input by inputting text
  await userEvent.type(chocolateInput, "2");
  //^^this line of code does not work
  // fireEvent.change(chocolateInput, {
  //   target: { value: "2" },
  // });
  //checks to see what the subtotal is after chocolate scoop
  expect(scoopsSubtotal).toHaveTextContent("6.00");
});

test("subtotal for toppings", async () => {
  //render parent component
  render(<Options optionType={"toppings"} />);

  //makes sure the total starts at 0.00
  const toppingsSubtotal = screen.getByText("Toppings total: $", {
    exact: false,
  });
  expect(toppingsSubtotal).toHaveTextContent("0.00");

  //initialization
  const CherryBox = await screen.findByRole("checkbox", {
    name: "Cherries",
  });
  //checks the box for cherries and checks the subtotal
  await userEvent.click(CherryBox);
  expect(CherryBox).toBeChecked();
  expect(toppingsSubtotal).toHaveTextContent("1.50");

  await userEvent.click(CherryBox);
  expect(CherryBox).not.toBeChecked();
  expect(toppingsSubtotal).toHaveTextContent("0.00");

  const MandMsBox = await screen.findByRole("checkbox", {
    name: "M&Ms",
  });
  await userEvent.click(MandMsBox);
  expect(MandMsBox).toBeChecked();
  expect(toppingsSubtotal).toHaveTextContent("1.50");
  const HotFudgeBox = await screen.findByRole("checkbox", {
    name: "Hot fudge",
  });
  await userEvent.click(HotFudgeBox);
  expect(HotFudgeBox).toBeChecked();
  expect(toppingsSubtotal).toHaveTextContent("3.00");
});

describe("grand total", () => {
  test("grandtotal starts at 0.00", async () => {
    render(<OrderEntry />);

    const grandtotal = screen.getByRole("heading", {
      name: /grand total: \$/i,
    });
    expect(grandtotal).toHaveTextContent("$0.00");
  });
  test("grandtotal updates properly if scoop is added first", async () => {
    render(<OrderEntry />);

    const scoopsSubtotal = screen.getByText("Scoops total: $", {
      exact: false,
    });
    expect(scoopsSubtotal).toHaveTextContent("0.00");

    //updates vanilla scoops to 1 and check the subtotal
    const vanillaInput = await screen.findByRole("spinbutton", {
      name: "Vanilla",
    });

    //clears vanilla input
    userEvent.clear(vanillaInput);
    //changes the value for input by inputting text
    await userEvent.type(vanillaInput, "2");
    expect(scoopsSubtotal).toHaveTextContent("4.00");

    const chocolateInput = await screen.findByRole("spinbutton", {
      name: "Chocolate",
    });

    //clears vanilla input
    userEvent.clear(chocolateInput);
    //changes the value for input by inputting text
    await userEvent.type(chocolateInput, "2");
    expect(scoopsSubtotal).toHaveTextContent("8.00");
  });
  test("grandtotal updates properly if topping is added first", async () => {
    //render parent component
    render(<OrderEntry />);

    //makes sure the total starts at 0.00
    const toppingsSubtotal = screen.getByText("Toppings total: $", {
      exact: false,
    });
    expect(toppingsSubtotal).toHaveTextContent("0.00");

    //initialization
    const CherryBox = await screen.findByRole("checkbox", {
      name: "Cherries",
    });
    //checks the box for cherries and checks the subtotal
    await userEvent.click(CherryBox);
    expect(CherryBox).toBeChecked();
    expect(toppingsSubtotal).toHaveTextContent("1.50");
    await userEvent.click(CherryBox);
    expect(CherryBox).not.toBeChecked();
    expect(toppingsSubtotal).toHaveTextContent("0.00");

    const MandMsBox = await screen.findByRole("checkbox", {
      name: "M&Ms",
    });
    await userEvent.click(MandMsBox);
    expect(MandMsBox).toBeChecked();
    expect(toppingsSubtotal).toHaveTextContent("1.50");
  });
  test("grand total updates properly if an item is removed", async () => {
    render(<OrderEntry />);

    //initialization
    const CherryBox = await screen.findByRole("checkbox", {
      name: "Cherries",
    });
    //checks the box for cherries and checks the subtotal
    await userEvent.click(CherryBox);
    expect(CherryBox).toBeChecked();

    //updates vanilla scoops to 1 and check the subtotal
    const vanillaInput = await screen.findByRole("spinbutton", {
      name: "Vanilla",
    });

    //clears vanilla input
    userEvent.clear(vanillaInput);
    //changes the value for input by inputting text
    await userEvent.type(vanillaInput, "2");
    //clears vanilla input
    userEvent.clear(vanillaInput);
    //changes the value for input by inputting text
    await userEvent.type(vanillaInput, "1");

    const grandTotal = screen.getByRole("heading", { name: /Grand total: \$/ });
    expect(grandTotal).toHaveTextContent("3.50");
  });
});
