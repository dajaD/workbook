import {
  render,
  screen,
  waitFor,
  waitForElementToBeRemoved,
} from "../../../test-utils/testing-library-utils";
import SummaryForm from "../SummaryForm";
import userEvent from "@testing-library/user-event";

test("checking initial conditions", () => {
  render(<SummaryForm />);

  const checkbox = screen.getByRole("checkbox", {
    name: /terms and conditions/i,
  });
  expect(checkbox).not.toBeChecked();

  const confirmbutton = screen.getByRole("button", {
    name: /confirm order/i,
  });
  expect(confirmbutton).toBeDisabled();
});

//userEvent > fireEvent because simulates more complete and realistic
//following the training realized there was an error when changing from fireEvent to userEvent
//there is a possible problem with react code where the checkmark isn't being interacted with
//not able to look at the webpage, doesn't run locally :

test("checkbox and button functionaility", async () => {
  render(<SummaryForm />);

  //checkbox
  const checkbox = screen.getByRole("checkbox", {
    name: /terms and conditions/i,
  });
  //button
  const confirmbutton = screen.getByRole("button", {
    name: /confirm order/i,
  });

  //clicks the the checkbox
  await userEvent.click(checkbox);
  //makes the test pass
  // fireEvent.click(checkbox);
  //checks to see if the checkbox has been checked
  expect(checkbox).toBeChecked();
  // expect(checkbox).toHaveProperty("checked", true);
  //checks to see if the confirmbutton is enabled
  expect(confirmbutton).toBeEnabled();

  //clicks the checkbox
  //makes the test fail
  await userEvent.click(checkbox);
  //only using fireEvent so the test can pass
  // fireEvent.click(checkbox);
  // expect(checkbox).toHaveProperty("checked", false);
  expect(checkbox).not.toBeChecked();
  expect(confirmbutton).toBeDisabled();
});

test("popover responds to hover", async () => {
  render(<SummaryForm />);

  //popover starts out
  // slashes mean it's a regular expression
  //case senstive
  const nullPopover = screen.queryByText(/no ice will actually be delivered/i);
  expect(nullPopover).not.toBeInTheDocument();

  //popover appears upon moverover of checkbox label
  const termsAndConditions = screen.getByText(/terms and conditions/i);
  userEvent.hover(termsAndConditions);

  //if this doesn't exist will throw, and the following line will never happen
  const popover = screen.getByText(/no ice cream will actually be delivered/i);
  //checks to see if it is in the document
  //best pratice to include this line to make it easier to read
  //doesn't serve any funcctional purpose
  expect(popover).toBeInTheDocument();

  //popover disappears when we mouse out
  userEvent.unhover(termsAndConditions);
  //query by text for the popover
  //acts an assertion asychronous
  waitForElementToBeRemoved(() =>
    screen.queryByText(/no ice cream will actually be delivered/i)
  );
});

//wasn't working originally because popover was disappearing asycchronouusly
