

import Button from "../Button/button";

import "./loginform.css";



function LoginForm({userType, setUserType}) {
    return (
     <div className="customer-box" id="customerBox">
      <div className="login-container" id="login">
        <div className="form-box">
          <div className="top" id="btns">
            <h2>{userType}</h2>
          </div>
          <form id="loginForm">
            <div className="two-forms">
              <input
                type="text"
                id="userType"
                hidden
                value=""
                name="userType"
              />

              <div className="input-box">
                <input
                  type="text"
                  className="input-field"
                  placeholder="username@gmail.com"
                  id="email"
                  name="email"
                  required
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