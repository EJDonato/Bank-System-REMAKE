
const logoutBtn = document.getElementById("logoutBtn");
logoutBtn.addEventListener("click", logout);

function logout() {
    window.location.href = "/";
}
