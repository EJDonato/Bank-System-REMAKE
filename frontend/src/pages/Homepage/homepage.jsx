import { useState, useEffect } from "react";

import "./homepage.css";

import Navbar from "../../components/Navbar/navbar";

function Homepage() {
  const [user, setUser] = useState();

  useEffect(() => {
    fetchUserData();
  }, []);

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

      <div className="wrapper">
        <div className="buttons">
          <button>Transact With Teller</button>
          <button>Request Loan</button>
          <button>Use ATM</button>
        </div>
      </div>
    </div>
  );
}

export default Homepage;
