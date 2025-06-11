import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Button from "../Button/button";

import "./signupform.css";

function SignupForm({ userType, setUserType, setSigningup }) {
const navigate = useNavigate();

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [bdate, setBdate] = useState("");

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repassword, setRepassword] = useState("");

  const [monthlySalary, setMonthlySalary] = useState("");
  const [pin, setPin] = useState("");
  const [startBalance, setStartBalance] = useState("");

  const goback = () => {
    console.log("GOO BAACKKK");
    setSigningup((prev) => !prev);
  };

  const signup = async (e) => {
    e.preventDefault();
    console.log("Signing up");

    const signupform = new FormData();
    console.log({
  firstName, lastName, bdate, email, password, monthlySalary, pin, startBalance, userType
});
    signupform.append("firstName", firstName);
    signupform.append("lastName", lastName);
    signupform.append("bdate", bdate);
    signupform.append("email", email);
    signupform.append("password", password);
    signupform.append("monthlySalary", monthlySalary);
    signupform.append("pin", pin);
    signupform.append("startBalance", startBalance);
    signupform.append("userType", userType);

    for (let pair of signupform.entries()) {
  console.log(pair[0] + ": " + pair[1]);
}

    try {
        const response = await fetch("http://127.0.0.1:5000/api/sign_up_info", {
        method: "POST",
        body: signupform
        })

        if (!response.ok) {
            throw new Error("Sign up failed. Please try again.")
        }

        navigate("/pending_account")
    }
    catch (error) {
        alert (error.message || "Something went wrong.")
    }
  };

  return (
    <div>
      <h2>Start Your Banking Journey With Us!</h2>
      <div className="signup-box" id="SignupBox">
        <div className="signup-container" id="signup">
          <form className="signup-container" id="signupForm" onSubmit={signup}>
            <div className="inputbox">
              <div className="forms">
                <div className="form-field">
                  <label htmlFor="first-name">First Name</label>
                  <input
                    type="text"
                    id="firstName"
                    placeholder="First Name"
                    required
                    name="firstName"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="last-name">Last Name</label>
                  <input
                    type="text"
                    id="lastName"
                    placeholder="Last Name"
                    required
                    name="lastName"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="bdate">Birthdate</label>
                  <input
                    type="date"
                    id="bdate"
                    required
                    name="bdate"
                    value={bdate}
                    onChange={(e) => setBdate(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="email">Email</label>
                  <input
                    type="text"
                    id="email"
                    placeholder="email@gmail.com"
                    required
                    name="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="password">Password</label>
                  <input
                    type="password"
                    id="password"
                    placeholder="Password"
                    required
                    name="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="re-password">Re-enter Password</label>
                  <input
                    type="password"
                    id="repassword"
                    placeholder="Re-enter Password"
                    required
                    value={repassword}
                    onChange={(e) => setRepassword(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="monthly_salary">Monthly Salary</label>
                  <input
                    type="number"
                    id="monthlySalary"
                    required
                    name="monthlySalary"
                    value={monthlySalary}
                    onChange={(e) => setMonthlySalary(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="pin">Bank Account Pin</label>
                  <input
                    type="number"
                    id="pin"
                    required
                    name="pin"
                    value={pin}
                    onChange={(e) => setPin(e.target.value)}
                  />
                </div>
                <div className="form-field">
                  <label htmlFor="start_bal">Starting Balance</label>
                  <input
                    type="number"
                    id="startBalance"
                    required
                    name="startBalance"
                    value={startBalance}
                    onChange={(e) => setStartBalance(e.target.value)}
                  />
                </div>
              </div>

              <div className="button-container">
                <Button
                  text={"Sign Up"}
                  className={"signupBtn"}
                  type={"submit"}
                />
                <Button
                  text={"Go Back"}
                  className={"signupBtn"}
                  onClick={goback}
                  type={"button"}
                />
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupForm;
