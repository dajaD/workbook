import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import ScoopOption from "../ScoopOption";

test("red input box for invalid scoops count", async () => {
  //needs a mock function 'updateItemCount ---> scoop option will run update item
  //count whenever the input
  //has been changed ---> prop will give errors when running test without it
  //has a name and image path ---> test would pass without these; makes typescrpt happy
  render(<ScoopOption name="" imagePath="" updateItemCount={jest.fn()} />);

  //should pass because this is outside of range
  //doesn't need the await is because it gets information from the prop
  //finds the spin button that is available on the page
  const chocolateInput = screen.getByRole("spinbutton");
  userEvent.clear(chocolateInput);
  userEvent.type(chocolateInput, "-2");
  expect(chocolateInput).toHaveClass("is-invalid");

  //should pass because this is outside of range
  userEvent.clear(chocolateInput);
  userEvent.type(chocolateInput, "2.5");
  expect(chocolateInput).toHaveClass("is-invalid");

  //should pass because outside of accecptabe range
  userEvent.clear(chocolateInput);
  userEvent.type(chocolateInput, "11");
  expect(chocolateInput).toHaveClass("is-invalid");

  //should fail as this is an appropriate response
  //tests to make sure the valid input works with validation
  userEvent.clear(chocolateInput);
  userEvent.type(chocolateInput, "2");
  expect(chocolateInput).toHaveClass("is-invalid");
});

//need react code for the test to actually pass (scoop option)
//create-react-app, has known issues with vulnerabilities
//tests work then stop working due to react codes, tests should pass in future
//without using create-react-app
//https://github.com/facebook/create-react-app/issues/11174
