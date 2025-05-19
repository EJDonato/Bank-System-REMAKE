
const customerBtn = document.getElementById('customerbtn');
const tellerBtn = document.getElementById('tellerbtn');
const managerBtn = document.getElementById('managerbtn');

const wrapper = document.querySelector('.wrapper');
const customerBox = document.getElementById('customerBox');

const userType = document.getElementById('userType');

// SET USER TYPE
customerBtn.addEventListener('click', () => {
  wrapper.style.display = 'none'; 
  customerBox.style.display = 'block'; 

  userType.value = 'customer';
});

tellerBtn.addEventListener('click', () => {
  wrapper.style.display = 'none'; 
  customerBox.style.display = 'block'; 

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

const loginForm = document.getElementById('loginForm');

function login() {
  if (!loginForm.checkValidity()) {
        // This triggers the browser's built-in validation UI automatically
        loginForm.reportValidity();
        return; // stop submission if invalid
    }

  const loginFormData = new FormData(loginForm);

  fetch('/login_info', {
    method: 'POST',
    body: loginFormData
  })
  .then(response => response.json())
  .then(data => {
    redirect_url = data.redirect_url;
    window.location.href = redirect_url;
  })
}



