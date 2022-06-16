import { render } from "@testing-library/react";
import { OrderDetailsProvider } from "../contexts/OrderDetails";

//assists with automatic wrapping
//custom render
//takes a ui, and an options object
//will return render with a ui, and the render of orderdetailprovider and any other option object
const renderWithContext = (ui, options) =>
  render(ui, { wrapper: OrderDetailsProvider, ...options });

// re-export everything
export * from "@testing-library/react";

// overrides the render method with render with context
export { renderWithContext as render };

//to render with context will import from this file
