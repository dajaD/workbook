import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';
import { toHaveStyle } from '@testing-library/jest-dom';
import {replaceCamelCaseWithSpaces} from './App';



test('button has the correct inital color', () => {
  render(<App />)

  //find an element with a role of button and text of 'change to Midnight blue'
  const colorButton = screen.getByRole('button', { name: 'Change to Midnight Blue' });

  //expect the backgroud of the button to be red
  expect(colorButton).toHaveStyle({ backgroundColor: 'MediumVioletRed' });

  //click the button
  //uses the fireEvent
  fireEvent.click(colorButton);

  //expect the background color to be blue
  expect(colorButton).toHaveStyle({ backgroundColor: 'MidnightBlue' });

  //expect the button to be changed to red
  expect(colorButton.textContent).toBe('Change to Medium Violet Red');
});

//testing initial conditions
test('initial conditions', () => {
  render(<App />)

  //check that the button starts out enabled
  const colorButton = screen.getByRole('button', {name: 'Change to Midnight Blue'});
  expect(colorButton).toBeEnabled();

  //checks that the checkbox starts out unchecked
  const checkbox = screen.getByRole('checkbox');
  //expect that it starts out unchecked
  expect(checkbox).not.toBeChecked();
});

test('checkbox functionality', () => {
render(<App />)

//defines checkbox and the button
const checkbox = screen.getByRole('checkbox', {name: 'Disable Button'});
const Button = screen.getByRole('button', {name: 'Change to Midnight Blue'});

//checks the box and checks to make sure the button is disabled
fireEvent.click(checkbox);
expect(Button).toBeDisabled();

//checks the box and checks to make sure the button is enabled
fireEvent.click(checkbox);
expect(Button).toBeEnabled();
});

test('disabled click should turn button gray', () => {
  render(<App/>)

  //defines checkbox and the button
const checkbox = screen.getByRole('checkbox', {name: 'Disable Button'});
const Button = screen.getByRole('button', {name: 'Change to Midnight Blue'});  

//clicks the disabled checkbox and turns the button gray
fireEvent.click(checkbox)
expect(Button).toHaveStyle('background-color: gray');


//clicks the check box again enabling the button and turning the color red
fireEvent.click(checkbox)
expect(Button).toHaveStyle('background-color: MediumVioletRed');
});

test('disabled click > button click should turn button blue', () => {
  render(<App/>)

  //defines checkbox and the color button
const checkbox = screen.getByRole('checkbox', {name: 'Disable Button'});
const Button = screen.getByRole('button', {name: 'Change to Midnight Blue'});  

//clicks the disabled checkbox and turns the button gray
fireEvent.click(checkbox);
//checks to see if the button is actually green
expect(Button).toHaveStyle('background-color: gray');
//clicks the check box again to turn button red
fireEvent.click(checkbox);
expect(Button).toHaveStyle('background-color: MediumVioletRed')
//clicks the button to turn button blue
fireEvent.click(Button);
//checks to see if the button color is blue
expect(Button).toHaveStyle('background-color: MidnightBlue');
});

//combine the test in a describe statement
describe('spaces before camel-case capital letters', () =>{
  test('Works for no inner capital letters', () => {
    expect(replaceCamelCaseWithSpaces('Red')).toBe('Red');
  });
  
  test('works for one inner capital letters', () => {
    expect(replaceCamelCaseWithSpaces('MidnightBlue')).toBe('Midnight Blue')
  });
  
  test('Works for multiple inner capital letters', () => {
    expect(replaceCamelCaseWithSpaces('MediumVioletRed')).toBe('Medium Violet Red')
  });
});

//don't need the below line as it is checking in the above code
// test('button has the correct inital text', () => {

// // });
// test('button turns blue when clicked', () => {
//   render(<App />)
//   const colorButton = screen.getByRole('button', {name: 'Change to blue' });

// });