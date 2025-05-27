import { useState } from "react";
import { useNavigate } from "react-router-dom"

import Button from "../Button/button";

import {login} from "../../services/login.js";

import "./loginform.css";



function LoginForm({userType, setUserType}) {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const initlogin = async (e) => {
        e.preventDefault();
        const success = await login(email, password, userType)
        if (success) {
            // Redirect to homepage with userType and email
            navigate(success)
        } else {
            const errorMsg = document.getElementById('errorMsg');
            errorMsg.style.display = 'block'; // Show the error message
            errorMsg.textContent = "Login Failed"; // Display the error message
        }
    }

    return (
     <div className="customer-box" id="customerBox">
      <div className="login-container" id="login">
        <div className="form-box">
          <div className="top" id="btns">
            <h2>{userType}</h2>
          </div>
          <form id="loginForm" onSubmit={initlogin}>
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
                  No account? <a href="#" id="signUp_a">Sign up</a>
                </span>
              </div>
            </div>
          </form>
          <Button text={"Go Back"} className={"loginBtn"} onClick={() => setUserType("")}/>
        </div>
      </div>
    </div>
  );
}

export default LoginForm;