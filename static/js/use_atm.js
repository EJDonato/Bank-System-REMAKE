const ATMBtn = document.getElementById('ATMBtn');
const Backbtn = document.getElementById('Backbtn');
const ATMBackBtn = document.getElementById('ATMBackBtn');
const ATMBox = document.getElementById('ATMBox');
const welcomeSection = document.getElementById('welcomeSection');
  
ATMBtn.addEventListener('click', function () {
    welcomeSection.style.display = 'none';
    ATMBox.style.display = 'block';
});
  
ATMBackBtn.addEventListener('click', function () {
    welcomeSection.style.display = 'block';
    ATMBox.style.display = 'none';
});
  
  