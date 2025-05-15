
const customerBtn = document.getElementById('customerbtn');
const tellerBtn = document.getElementById('tellerbtn');
const managerBtn = document.getElementById('managerbtn');

const wrapper = document.querySelector('.wrapper');
const customerBox = document.getElementById('customerBox');

const userType = document.getElementById('userType');


customerBtn.addEventListener('click', () => {
  wrapper.style.display = 'none'; 
  customerBox.style.display = 'block'; 

  userType.value = 'customer';
});


// SET USER TYPE
tellerBtn.addEventListener('click', () => {
  userType.value = 'teller';
})

managerBtn.addEventListener('click', () => {
  userType.value = 'manager';
})

// WHEN U CLICK THE SIGN UP ANCHOR
const go_to_signUp_a = document.getElementById("signUp_a");
go_to_signUp_a.addEventListener("click", () => {
  console.log(userType.value);
  window.location.href = `/sign_up/${userType.value}`;
});



// LOGIN
const loginBtn = document.getElementById('loginBtn');
loginBtn.addEventListener('click', login);

function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  fetch('/login_info', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "email": email, 
      "password": password 
    })
  })
  .then(response => response.json())
  .then(data => {
    // DIPA TO TAPOS
  })
}



