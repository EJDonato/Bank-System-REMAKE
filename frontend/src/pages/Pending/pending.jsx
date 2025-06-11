import { useNavigate } from "react-router-dom";

import Button from "../../components/Button/button";

import "./pending.css";

function Pending() {
  const navigate = useNavigate();
  const logOut = () => {
    navigate("/");
  };

  return (
    <div className="container">
      <div className="loader"></div>
      <div className="text">
        <h1>Account Creation in Progress</h1>
        <p>
          Your bank account creation request is currently pending approval.
          Please check back soon.
        </p>
      </div>
      <div className="buttons">
        <Button id={"logoutBtn"} text={"Log Out"} onClick={logOut} />
      </div>
    </div>
  );
}

export default Pending;
