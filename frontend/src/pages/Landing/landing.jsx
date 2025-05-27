import { useState } from "react"

import Navbar from "../../components/Navbar/navbar"
import Button from "../../components/Button/button"
import LoginForm from "../../components/LoginForm/loginform"  

import "./landing.css"



function Landing() {
    const [userType, setUserType] = useState("");

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

            {userType && <LoginForm userType={userType} setUserType={setUserType}/>}
        </div>
    )
}

export default Landing;