import { useState, useEffect } from "react";

import "./homepage.css";

import Navbar from "../../components/Navbar/navbar";
import EnterPin from "../../components/EnterPin/enterpin";
import Button from "../../components/Button/button";
import ATM from "../../components/ATM/atm";

function Homepage() {
  const [user, setUser] = useState();

  const [isUseAtmPin, setIsUseAtmPin] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const [refetch, setRefetch] = useState(false);
  const refreshData = () => {
    setRefetch(prev => !prev)
  }

  const useATM = () => {
    setIsUseAtmPin((prev) => !prev);
  };

  useEffect(() => {
    fetchUserData();
  }, [refetch]);

  const fetchUserData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/user_info", {
        credentials: "include",
      });

      if (!response.ok) {
        // Handle HTTP error response
        const errorData = await response.json();
        throw new Error(errorData.error || "Login failed");
      }

      const data = await response.json();
      setUser(data);
    } catch (error) {
      console.error("Login error:", error.message);
      const errorMsg = document.getElementById("errorMsg");
    }
  };
  console.log("User logged in is ", user);

  return (
    <div>
      <Navbar />

      <h1>My Bank Account</h1>

      {user && (
        <div className="wrapper">
          <div className="acc_infocard">
            <h3>
              {user.first_name} {user.last_name}
            </h3>

            <div>
              <label htmlFor="acc_num">Account Number: </label>
              <p id="acc_num">{user.account_number}</p>
            </div>

            <div>
              <label htmlFor="acc_bal">Balance: </label>
              <p id="acc_bal">₱{user.balance}</p>
            </div>
          </div>
        </div>
      )}

      {!isAuthenticated && (
        <div className="wrapper">
          <div className="buttons">
            <Button text={"Transact With Teller"} className={"button"} />
            <Button text={"Request Loan"} className={"button"} />
            <Button text={"Use ATM"} className={"button"} onClick={useATM} />
          </div>
        </div>
      )}

      {isUseAtmPin && (
        <EnterPin
          useATM={useATM}
          user={user}
          setIsAuthenticated={setIsAuthenticated}
        />
      )}
      {isAuthenticated && (
        <ATM setIsAuthenticated={setIsAuthenticated} user={user} refetch={refreshData}/>
      )}
    </div>
  );
}

export default Homepage;
