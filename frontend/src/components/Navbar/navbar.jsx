
import "./navbar.css"

function Navbar() {
    return (
    <div>
        <header class="nav">
            <div class="logo">
                <p>InspirePay</p>
            </div>
            <div class="nav-menu">
                <ul>
                    <li><a href="#about" class="link">About</a></li>
                    <li><a href="#services" class="link">Services</a></li>
                    <li><a href="#contact" class="link">Contact</a></li>
                    <li><a href="#home" class="link">Home</a></li>
                </ul>
            </div>
        </header>
    </div>
    )
}


export default Navbar;