import {
  render,
  screen,
  waitFor,
} from "../../../test-utils/testing-library-utils";
import OrderEntry from "../OrderEntry";
import userEvent from "@testing-library/user-event";
import { rest } from "msw";
import { server } from "../../../mocks/server";

//if using await need to make function async
//if there are multiple test and only one want to test one, would use test.only
test("handles error for scoops and toppings routes", async () => {
  //will reset handlers
  server.resetHandlers(
    rest.get("http://localhost:3030/scoops", (req, res, ctx) =>
      res(ctx.status(500))
    ),
    rest.get("http://localhost:3030/toppings", (req, res, ctx) =>
      res(ctx.status(500))
    )
  );

  render(<OrderEntry setOrderPhase={jest.fn()} />);

  //because the alerts are expected to be there asyncronously
  //will not appear until hit catch function on axios
  //need to use await when using .findAllbyRole
  await waitFor(async () => {
    const alerts = await screen.findAllByRole("alert");

    //will be two expects because there is an alert for scoops and toppings
    expect(alerts).toHaveLength(2);
  });
});

test("Order phases for happy path with no scoops, button should be disabled", async () => {
  //render app
  //need the setOrderPhase prop for typescript
  render(<OrderEntry setOrderPhase={jest.fn()} />);

  //orderbutton should start off disabled since there are no scoops
  const orderButton = screen.getByRole("button", { name: /order sundae/i });
  screen.debug();
  expect(orderButton).toHaveAttribute("disabled");

  //adds 2 scoops to the chocolateInput
  const chocolateInput = await screen.findByRole("spinbutton", {
    name: "Chocolate",
  });
  await userEvent.clear(chocolateInput);
  await userEvent.type(chocolateInput, "2");
  screen.debug();
  expect(orderButton).toBeEnabled();

  // removes the two scoops for the chocolateInput
  await userEvent.clear(chocolateInput);
  await userEvent.type(chocolateInput, "0");
});
