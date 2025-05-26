
const logOutBtn = document.getElementById("logOut")
logOutBtn.addEventListener("click", logOut)

async function logOut() { 
    const response = await fetch("/logout", {
        method: "POST",
        credentials: "same-origin"
    });

    if (response.ok) {
        window.location.href = "/"
    }
}
