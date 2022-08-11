/**
 * //type to expect
 * @function formatCurrency
 * Format number as currency (US Dollars)
 *
 * //type to return
 * @param {number} currency
 * @returns {string} number formatted as currency.
 *
 *
 * //example on how it works
 * @example
 *   formatCurrency(0)
 *   // => $0.00
 *
 * @example
 *   formatCurrency(1.5)
 *   // => $1.50
 *
 */
// //function that will format the currency to solve the error:  FAIL  src/pages/entry/tests/totalUpdates.test.jsx
// //  × update scoop subtotal when scoops change (69 ms)
// //  ● update scoop subtotal when scoops change
// // TestingLibraryElementError: Unable to find an element with the text: Scoops total: $.
// //This could be because the text is broken up by multiple elements. In this case, you can provide a
// //function for your text matcher to make your matcher more flexible.
export function formatCurrency(amount) {
  //intl: international number format -> javascript builtin function

  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format(amount);
}
