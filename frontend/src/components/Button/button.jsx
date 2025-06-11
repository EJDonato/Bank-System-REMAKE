
import "./button.css";

function Button({ text, onClick, className, type, id}) {
    return (
        <button className={`${className}`} onClick={onClick} type={type} id={id}>
            {text}
        </button>
    );
}

export default Button;