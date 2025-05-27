
import "./homepage.css";

import Navbar from "../../components/Navbar/navbar";

import {getUserInfo} from "../../services/login.js";


function Homepage() {
    const user = getUserInfo();
    console.log(user);

    return (
        <div>
            <Navbar />
            <h1>My Bank Account</h1>

            <div className="wrapper">
                <div className="acc_infocard">
                    <h3>{ user.first_name }</h3>
        
                    <div>
                        <label htmlFor="acc_num">Account Number: </label>
                        <p id="acc_num">{ user.account_number }</p>
                    </div>
                    
                    <div>
                        <label htmlFor="acc_bal">Balance: </label>
                        <p id="acc_bal">₱{ user.balance }</p>
                    </div>
                </div>
            </div>
            
            <div className="wrapper">
                <div className="buttons">
                    <button>Transact With Teller</button>
                    <button>Request Loan</button>
                    <button>Use ATM</button>
                </div>
            </div>
        </div>
    )
}

export default Homepage;