import { useState } from "react";
import { useNavigate } from "react-router-dom"

import Button from "../Button/button";

import "./loginform.css";



function LoginForm({userType, setUserType, setSigningup}) {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const gotosignup = () => {
      console.log("GO TO SIGNUPPP")
      setSigningup(prev => !prev)
    }

    const login = async (e) => {
        e.preventDefault(); // Prevent the default form submission

        const loginForm = new FormData()
        loginForm.append('email', email);
        loginForm.append('password', password);
        loginForm.append('userType', userType.toLowerCase());

        console.log("Login Form Data:", Object.fromEntries(loginForm.entries()));

        try {
            const response = await fetch('http://127.0.0.1:5000/api/login_info', {
            method: 'POST',
            body: loginForm,
            credentials: 'include' // Include cookies for session management
        });
            if (!response.ok) {
                // Handle HTTP error response
                const errorData = await response.json();
                throw new Error(errorData.error || "Login failed");
            }

            const data = await response.json();
            const redirect_url = data.redirect_url;
            console.log("Redirecting to:", redirect_url);

            navigate(redirect_url); // Use navigate to redirect
        } catch (error) {
            console.error("Login error:", error.message);
            const errorMsg = document.getElementById("errorMsg");
            errorMsg.textContent = error.message; // Show error message to user
            errorMsg.style.display = "block"; // Make the error message visible
    }
  }

    return (
     <div className="customer-box" id="customerBox">
      <div className="login-container" id="login">
        <div className="form-box">
          <div className="top" id="btns">
            <h2>{userType}</h2>
          </div>
          <form id="loginForm" onSubmit={login}>
            <div className="two-forms">
              <div className="input-box">
                <input
                    type="text"
                    className="input-field"
                    placeholder="username@gmail.com"
                    id="email"
                    name="email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div className="input-box">
                <input
                    type="password"
                    className="input-field"
                    placeholder="Password"
                    id="password"
                    name="password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
              </div>

              <p
                id="errorMsg"
                style={{ display: "none", color: "red" }}
              ></p>

              <div className="login-box">
                <Button text={"Login"} className={"loginBtn"}/>
              </div>
              <div className="col">
                <input type="checkbox" id="login-check" />
                <label htmlFor="login-check">Remember Me</label>
              </div>
              <div className="top">
                <span>
                  No account? <Button type={"button"} text={"Sign Up"} className={"signupA"} onClick={gotosignup} />
                </span>
              </div>
            </div>
          </form>
          <Button text={"Go Back"} className={"loginBtn"} onClick={() => setUserType("")}/>
        </div>
      </div>
    </div>
  );
};
    
export default LoginForm;