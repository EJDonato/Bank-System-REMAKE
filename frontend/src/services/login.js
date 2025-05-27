

async function login(email, password, userType) {

    if (!loginForm.checkValidity()) {
        // This triggers the browser's built-in validation UI automatically
        loginForm.reportValidity();
        return; // stop submission if invalid
    }

    const loginFormData = new FormData();
    loginFormData.append('email', email);
    loginFormData.append('password', password);
    loginFormData.append('userType', userType.toLowerCase());

    console.log("Login Form Data:", Object.fromEntries(loginFormData.entries()));

    try {
        const response = await fetch('http://127.0.0.1:5000/login_info', {
            method: 'POST',
            body: loginFormData,
            credentials: 'include' // Include cookies for session management
        });

        const data = await response.json();

        if (!response.ok) {
            // Handle HTTP error response
            throw new Error(data.error || "Login failed");
        }

        const redirect_url = data.redirect_url;
        console.log("Redirecting to:", redirect_url);
        return redirect_url;
    } catch (error) {
        console.error("Login error:", error.message);
        alert(error.message); // Show error message to user
    }

}


async function getUserInfo() {
    const response = await fetch('http://127.0.0.1:5000/api/user_info',{
        method: 'GET',
        credentials: 'include' // Include cookies for session management
    });

    if (!response.ok) {
        throw new Error('Failed to fetch user info');
    }

    const data = await response.json();
    console.log("User Info:", data);
    return data; // Return the user info
}


export {login, getUserInfo};
