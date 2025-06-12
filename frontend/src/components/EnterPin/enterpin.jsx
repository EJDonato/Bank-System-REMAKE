import { useState } from "react";
import Button from "../Button/button";

import "./enterpin.css";

function EnterPin({ useATM, user, setIsAuthenticated }) {
  const [accNumber, setAccNum] = useState(user.account_number);
  const [pin, setPin] = useState("");

  const checkPin = async () => {
    const pinForm = new FormData();
    pinForm.append("pin", pin);
    pinForm.append("acc_num", accNumber);

    useATM() // Remove Enter Pin from view

    try {
      const response = await fetch("http://127.0.0.1:5000/api/check_pin", {
        method: "POST",
        body: pinForm,
        credentials: "include", // Include cookies for session management
      });
      if (!response.ok) {
        // Handle HTTP error response
        const errorData = await response.json();
        throw new Error(errorData.error || "Wrong Pin");
      }

      const data = await response.json();
      console.log(data);
      if (data.result === true) {
        setIsAuthenticated(true)
      }

    } catch (error) {
      console.error("Error:", error.message);
    }
  };

  return (
    <div className="enterpin-container">
      <div className="enter-pin">
        <label htmlFor="pin">Enter Pin: </label>
        <input
          type="password"
          id="pin"
          placeholder="XXXXXX"
          value={pin}
          onChange={(e) => setPin(e.target.value)}
        />
      </div>
      <div className="atm-buttons">
        <Button text={"Use ATM"} className={"useAtm"} onClick={checkPin} />
        <Button text={"Back"} className={"useAtm"} onClick={useATM} />
      </div>
    </div>
  );
}

export default EnterPin;
