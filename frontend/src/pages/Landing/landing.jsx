import "./landing.css"

import Navbar from "../../components/Navbar/navbar"
import Button from "../../components/Button/button"

function Landing() {
    return (
        <div>
            <Navbar />

            <div className="btn-container">
                <Button text={"Customer"} className={"button"}/>
                <Button text={"Teller"} className={"button"}/>
                <Button text={"Manager"} className={"button"}/>
            </div>
        </div>
        
    )
}

export default Landing;