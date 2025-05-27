
import "./navbar.css"

function Navbar() {
    return (
    <div>
        <header className="nav">
            <div className="logo">
                <p>InspirePay</p>
            </div>
            <div className="nav-menu">
                <ul>
                    <li><a href="#about" className="link">About</a></li>
                    <li><a href="#services" className="link">Services</a></li>
                    <li><a href="#contact" className="link">Contact</a></li>
                    <li><a href="#home" className="link">Home</a></li>
                </ul>
            </div>
        </header>
    </div>
    )
}


export default Navbar;