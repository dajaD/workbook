// import logo from './logo.svg';
import './App.css';
import { useState } from 'react'
// import { toBeDisabled, toBeEnabled } from '@testing-library/jest-dom/dist/matchers';

export function replaceCamelCaseWithSpaces(colorName) {
  return colorName.replace(/\B([A-Z])\B/g, ' $1');
}

export function changeLetters(colorName){
  return colorName.replace('$1');
}

function App() {
  const [ buttonColor, setButtonColor ] = useState('MediumVioletRed');

  //boolean state called disabled and setDisabled
  //starts off as false
  const [ disabled, setDisabled ] = useState(false);
  const newButtonColor = buttonColor === 'MediumVioletRed' ? 'Midnight.Blue' : 'MediumVioletRed';

  return (
   <div>
     {/* button 
     default check to disabled
     aria-check, allows for screen readers to see if its disabled
     onchange works for the click on the input*/}
     <button
      style={{backgroundColor: disabled ? 'gray' : buttonColor}}
      onClick = {() => setButtonColor(newButtonColor)}
      disabled = {disabled}
      >Change to {replaceCamelCaseWithSpaces(newButtonColor) }</button>
      <br />
      <input 
       type='checkbox'
       id = 'disable-button-checkbox'
       defaultChecked={disabled}
       aria-checked={disabled}
       onChange={((e) => setDisabled(e.target.checked))}/>
       <label htmlFor='disable-button-checkbox'>
        Disable Button
      </label>
   </div>

  );
}

export default App;