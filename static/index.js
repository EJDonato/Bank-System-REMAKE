const customerBtn = document.getElementById("customerbtn");
const wrapper = document.querySelector(".wrapper");
const customerBox = document.getElementById("customerBox");
const backBtn = document.getElementById("backBtn");

customerBtn.addEventListener("click", () => {
  wrapper.style.display = "none";
  customerBox.style.display = "block";
});

backBtn.addEventListener("click", () => {
  customerBox.style.display = "none";
  wrapper.style.display = "flex";
});

// LOGIN FUNCTION
const loginBtn = document.getElementById("loginBtn");
loginBtn.addEventListener("click", login);

function login() {
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  fetch("/customer_login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      let response = data.result;
      let acc_name = data.acc_name;

      if (response == true) {
        window.location.href = `/homepage/${acc_name}`;
      }
    })
    .catch((error) => {
      console.error("Login Error", error);
    });
}
