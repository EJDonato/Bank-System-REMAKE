
const signUpBtn = document.getElementById("signUpBtn");
signUpBtn.addEventListener("click", signUp);

const signupForm = document.getElementById("signupForm");

async function signUp() {
    if (!signupForm.checkValidity()) {
        // This triggers the browser's built-in validation UI automatically
        signupForm.reportValidity();
        return; // stop submission if invalid
    }

    const signupFormData = new FormData(signupForm);

    // Insert password repassword matching check here

    try {
        const response = await fetch("/sign_up_info", {
        method: "POST",
        body: signupFormData
        })

        if (!response.ok) {
            throw new Error("Sign up failed. Please try again.")
        }

        window.location.href = "/pending_account"
    }
    catch (error) {
        alert (error.message || "Something went wrong.")
    }
    
}

