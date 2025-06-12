import "./atm.css";

import Button from "../Button/button";
import { useState } from "react";

function EnterValue({
  setIsEnteringValue,
  isDepositing,
  isWithdrawing,
  isChangingPin,
  user,
  refetch
}) {
  const [value, setValue] = useState("");
  const [currentBal, setCurrentBal] = useState(user.balance);

  const withdraw = () => {
    const newBal = Number(user.balance) - Number(value);
    updateBal(newBal)
  }
  const deposit = () => {
    const newBal = Number(user.balance) + Number(value);
    console.log("depositing, new bal is ", newBal)
    updateBal(newBal)
  }

  const updateBal = async (newBal) => {
    const form = new FormData()
    form.append("newBalance", newBal)
    form.append("accNum", user.account_number)

    try {
      const response = await fetch("http://127.0.0.1:5000/api/update_balance", {
        method: "POST",
        body: form,
        credentials: "include", // Include cookies for session management
      });
      if (!response.ok) {
        // Handle HTTP error response
        const errorData = await response.json();
        throw new Error(errorData.error || "Error Occurred");
      }

      const data = await response.json();
      console.log(data)

      refetch()

    } catch (error) {
      console.error("Error:", error.message);
    }
  };

  const submit = () => {
    if (isWithdrawing === true) {
      withdraw();
    }
    else if (isDepositing === true) {
      deposit()
    }

    setIsEnteringValue(false)
  };

  const goBack = () => {
    setIsEnteringValue(false);
  };

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
        <Button text={"Enter"} className={"useAtm"} onClick={submit}/>
        <Button text={"Back"} className={"useAtm"} onClick={goBack} />
      </div>
    </div>
  );
}

function ATM({ setIsAuthenticated, user, refetch }) {
  const [isDepositing, setIsDepositing] = useState(false);
  const [isWithdrawing, setIsWithdrawing] = useState(false);
  const [isChangingPin, setIsChangingPin] = useState(false);

  const [isEnteringValue, setIsEnteringValue] = useState(false);

  const withdraw = () => {
    setIsWithdrawing(true);
    setIsEnteringValue(true);
    setIsDepositing(false);
  };

  const deposit = () => {
    setIsDepositing(true);
    setIsEnteringValue(true);
    setIsWithdrawing(false);
  }

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
          <Button text={"Deposit"} className={"signupBtn"} onClick={deposit}/>
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
        {isEnteringValue && (
          <EnterValue
            setIsEnteringValue={setIsEnteringValue}
            isDepositing={isDepositing}
            isWithdrawing={isWithdrawing}
            isChangingPin={isChangingPin}
            user={user}
            refetch={refetch}
          />
        )}
      </div>
    </div>
  );
}

export default ATM;
