import {
  render,
  screen,
  waitFor,
} from "../../../test-utils/testing-library-utils";
//used ^^ as its already wrapped
import { server } from "../../../mocks/server";
import { rest } from "msw";
//^^ overrride mock server response

import OrderConfirmation from "../OrderConfirmation";

test("checking for error with order confirmation server", async () => {
  server.resetHandlers(
    rest.post("http://localhost:3030/order"),
    (req, res, ctx) => res(ctx.status(500))
  );
  //resets the handlers ^^
  render(<OrderConfirmation setOrderPhase={jest.fn()} />);
  //needs a prop

  await waitFor(async () => {
    const errorMessage = await screen.findByRole("alert");

    expect(errorMessage).toHaveTextContent(
      "An unexpected error occured. Please try again later."
    );
  });
});
