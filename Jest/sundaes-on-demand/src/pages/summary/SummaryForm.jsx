import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Popover from "react-bootstrap/Popover";

export default function SummaryForm() {
  //this is checked state
  //allows for tracking the 'state' of the checkbox via 'state'
  //allows for the enabled/disabled of button to function properly
  const [tcChecked, setTcChecked] = useState(false);

  //popover
  const popover = (
    <Popover id="termsandconditions-popover">
      <Popover.Body>No ice cream will actually be delivered</Popover.Body>
      {/* note: for React Bootstrap 2.x, the previous line needs to be:
      <Popover.Body>No ice cream will actually be delivered</Popover.Body>
      (replace Popover.Content with Popover.Body). For more details, see 
      https://www.udemy.com/course/react-testing-library/learn/lecture/30126784*/}
    </Popover>
  );

  //label for the checkbox
  //overlay trigger
  const checkboxLabel = (
    <span>
      I agree to
      <OverlayTrigger placement="right" overlay={popover}>
        <span style={{ color: "blue" }}> Terms and Conditions</span>
      </OverlayTrigger>
    </span>
  );
  //form
  //creates a group: 'form.group' which holds the checkbox
  //controlid allows for label
  //label is controlled by the above state.
  return (
    <Form>
      <Form.Group controlId="terms-and-conditions">
        <Form.Check
          type="checkbox"
          checked={tcChecked}
          onChange={(e) => setTcChecked(e.target.checked)}
          label={checkboxLabel}
        />
      </Form.Group>
      <Button variant="primary" type="submit" disabled={!tcChecked}>
        Confirm order
      </Button>
    </Form>
  );
}
