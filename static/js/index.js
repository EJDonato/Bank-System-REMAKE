
const customerBtn = document.getElementById('customerbtn');
const wrapper = document.querySelector('.wrapper');
const customerBox = document.getElementById('customerBox');
const backBtn = document.getElementById('backBtn');

customerBtn.addEventListener('click', () => {
  wrapper.style.display = 'none'; 
  customerBox.style.display = 'block'; 
});

backBtn.addEventListener('click', () => {
  customerBox.style.display = 'none'; 
  wrapper.style.display = 'flex'; 
});