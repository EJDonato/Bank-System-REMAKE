import "./atm.css";

import Button from "../Button/button";
import { useState } from "react";

function EnterValue({setIsEnteringValue}) {
  const [value, setValue] = useState("");

  const goBack = () => {
    setIsEnteringValue(false)
  }

  return (
    <div className="entervalue-container">
      <div className="enter-value">
        <label htmlFor="value">Enter Value: </label>
        <input
          type="number"
          id="value"
          placeholder="XXXXXX"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </div>
      <div className="valueButtons">
        <Button text={"Enter"} className={"useAtm"} />
        <Button text={"Back"} className={"useAtm"} onClick={goBack}/>
      </div>
    </div>
  );
}

function ATM({ setIsAuthenticated }) {
  const [isDepositing, setIsDepositing] = useState(false);
  const [isWithdrawing, setIsWithdrawing] = useState(false);

  const [isEnteringValue, setIsEnteringValue] = useState(false);

  const withdraw = () => {
    setIsWithdrawing(true);
    setIsEnteringValue(true);
  };

  const exitATM = () => {
    setIsAuthenticated(false);
  };

  return (
    <div className="main">
      <div className="atm-container">
        <h1>ATM Menu</h1>
        <div className="atm-buttons">
          <Button
            text={"Withdraw"}
            className={"signupBtn"}
            onClick={withdraw}
          />
          <Button text={"Deposit"} className={"signupBtn"} />
          <Button text={"Change Pin"} className={"signupBtn"} />
          <Button
            text={"Exit ATM"}
            className={"signupBtn"}
            id={"exit"}
            onClick={exitATM}
          />
        </div>
      </div>
      <div>
        {isEnteringValue && <EnterValue setIsEnteringValue={setIsEnteringValue}/>}
      </div>
    
    </div>
  );
}

export default ATM;
