import { useState } from "react";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";

export default function ScoopOption({ name, imagePath, updateItemCount }) {
  //added use state
  const [isValid, setIsValid] = useState(true);
  const handleChange = (event) => {
    const currentValue = event.target.value;
    //making sure using a number and not a string to validate ---> changes string to float
    const currentValueFloat = parseFloat(currentValue);

    //validation through onchange
    //this state is used in the react code
    const IsValid =
      //valueIsValid
      0 <= currentValueFloat &&
      currentValueFloat <= 10 &&
      //removes decimal and changes it to an integer
      Math.floor(currentValueFloat) === currentValueFloat;

    //validates the user input is actually valid
    setIsValid(IsValid);

    //should only update if the validation is good
    if (IsValid) updateItemCount(name, currentValue);
    //only update context if the value is valid
    // if (valueIsValid)
    //updateItemCount(name, currentValue);
  };

  return (
    <Col xs={12} sm={6} md={4} lg={3} style={{ textAlign: "center" }}>
      <img
        style={{ width: "75%" }}
        src={`http://localhost:3030/${imagePath}`}
        alt={`${name} scoop`}
      />
      <Form.Group
        controlId={`${name}-count`}
        as={Row}
        style={{ marginTop: "10px" }}
      >
        <Form.Label column xs="6" style={{ textAlign: "right" }}>
          {name}
        </Form.Label>
        <Col xs="5" style={{ textAlign: "left" }}>
          <Form.Control
            type="number"
            defaultValue={0}
            onChange={handleChange}
            isInvalid={!isValid}
          />
        </Col>
      </Form.Group>
    </Col>
  );
}
