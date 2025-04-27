
// Login Form Button
const loginbtn = document.getElementById("loginbtn")
loginbtn.addEventListener("click", login);
console.log(loginbtn)

function login() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    console.log("Email:", email, "Password:", password); // debug log

    fetch("/login/login_info", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "email":email,
            "password":password
        })
    })
    .then(response => response.json())
    .then(data => {
        let response = data.result
        let acc_name = data.acc_name

        if (response == true){
            window.location.href = `/homepage/${acc_name}`
        }
    })
    .catch(error => {
        console.error("Login Error", error)
    })
}

