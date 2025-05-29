
import "./button.css";

function Button({ text, onClick, className, type}) {
    return (
        <button className={`${className}`} onClick={onClick} type={type}>
            {text}
        </button>
    );
}

export default Button;