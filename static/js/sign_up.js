
const signUpBtn = document.getElementById("signUpBtn");
signUpBtn.addEventListener("click", signUp);

function signUp() {
    const first_name = document.getElementById("firstName").value;
    const last_name = document.getElementById("lastName").value;
    const bdate = document.getElementById("bdate").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const repassword = document.getElementById("repassword").value;
    const monthly_salary = document.getElementById("monthlySalary").value;
    const pin = document.getElementById("pin").value;
    const start_balance = document.getElementById("startBalance").value;
    const userType = document.getElementById("userType").value;

    // INSERT PASSWORD REPASSWORD CHECK HERE

    fetch("/sign_up_info", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "first_name": first_name,
            "last_name": last_name,
            "bdate": bdate,
            "email": email,
            "password": password,
            "monthly_salary": monthly_salary,
            "pin": pin,
            "start_balance": start_balance,
            "user_type": userType,
        }),
    })
}