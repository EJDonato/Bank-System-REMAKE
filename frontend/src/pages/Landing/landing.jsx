import { useState } from "react"

import Navbar from "../../components/Navbar/navbar"
import Button from "../../components/Button/button"
import LoginForm from "../../components/LoginForm/loginform"  
import SignupForm from "../../components/SignupForm/signupform"

import "./landing.css"



function Landing() {
    const [userType, setUserType] = useState("");
    const [signingup, setSigningup] = useState(false);

    const showLoginForm = (type) => setUserType(userType => type);

    return (
        <div>
            <Navbar />

            {!userType && 
                <div className="btn-container">
                    <Button text={"Customer"} className={"button"} onClick={() => showLoginForm("Customer")}/>
                    <Button text={"Teller"} className={"button"} onClick={() => showLoginForm("Teller")}/>
                    <Button text={"Manager"} className={"button"} onClick={() => showLoginForm("Manager")}/>
                </div>
            }

            {userType && !signingup && <LoginForm userType={userType} setUserType={setUserType} setSigningup={setSigningup}/>}
            {userType && signingup && <SignupForm userType={userType} setUserType={setUserType} setSigningup={setSigningup}/>}

        </div>
    )
}

export default Landing;