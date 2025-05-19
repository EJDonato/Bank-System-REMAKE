
const signUpBtn = document.getElementById("signUpBtn");
signUpBtn.addEventListener("click", signUp);

const signupForm = document.getElementById("signupForm");

function signUp() {
    if (!signupForm.checkValidity()) {
        // This triggers the browser's built-in validation UI automatically
        signupForm.reportValidity();
        return; // stop submission if invalid
    }

    const signupFormData = new FormData(signupForm);

    // INSERT PASSWORD REPASSWORD CHECK HERE

    fetch("/sign_up_info", {
        method: "POST",
        body: signupFormData
    })
    .then(response => {
        if (response.ok) {
            // Handle successful sign up response
            alert("Sign up successful!");
            window.location.href = "/pending_account";
        } else {
            // Handle error response
            alert("Sign up failed. Please try again.");
        }
    })
}