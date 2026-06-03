document
.getElementById('loginForm')
.addEventListener('submit', function(e){

    e.preventDefault();

    const email = document.querySelector('#email').value;
    const senha = document.querySelector('#senha').value;

    if(email === 'admin@sosmulher.com' && senha === '123456'){
        window.location.href = 'index.html';
    }else{
        alert('E-mail ou senha inválidos');
    }

});