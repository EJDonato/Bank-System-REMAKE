import { useState } from "react";
import { useNavigate } from "react-router-dom"

import Button from "../Button/button";

import "./signupform.css";


function SignupForm({userType, setUserType, setSigningup}) {

    const goback = () => {
      console.log("GOO BAACKKK")
      setSigningup(prev => !prev)
    }

    const signup = async (e) => {
        console.log("Signing up")
    }

    return (
        <div>
            <h2>Start Your Banking Journey With Us!</h2>
        <div class="signup-box" id="SignupBox">
            <div class="signup-container" id="signup">
                <form class="signup-container" id="signupForm">
                    <div class="inputbox">
                        <div class="forms">
                                <div class="form-field">
                                    <label htmlFor="first-name">First Name</label>
                                    <input type="text" id="firstName" placeholder="First Name" required name="firstName" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="last-name">Last Name</label>
                                    <input type="text" id="lastName" placeholder="Last Name" required name="lastName" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="bdate">Birthdate</label>
                                    <input type="date" id="bdate" required name="bdate" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="email">Email</label>
                                    <input type="text" id="email" placeholder="email@gmail.com" required name="email" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="password">Password</label>
                                    <input type="password" id="password" placeholder="Password" required name="password" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="re-password">Re-enter Password</label>
                                    <input type="password" id="repassword" placeholder="Re-enter Password" required />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="monthly_salary">Monthly Salary</label>
                                    <input type="number" id="monthlySalary" required name="monthlySalary" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="pin">Bank Account Pin</label>
                                    <input type="number" id="pin" required name="pin" />
                                </div>
                                <div class="form-field">
                                    <label htmlFor="start_bal">Starting Balance</label>
                                    <input type="number" id="startBalance" required name="startBalance" />
                                </div>
                        
                        </div>
            
                        <div class="button-container">
                            <Button text={"Sign Up"} className={"signupBtn"} onClick={signup}/>
                            <Button text={"Go Back"} className={"signupBtn"} onClick={goback} />
                        </div>
                    </div>
                </form>
            </div>
        </div>
        </div>
    )
};

export default SignupForm;