document.getElementById('form-login').addEventListener('submit', async function (form){
    form.preventDefault();
    
    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    const response = await fetch("http://127.0.0.1:8000/login", {
        method:'POST',
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify(data)
    });

    const resultado = await response.json();
    
    if (response.ok){
        window.location.replace('/home.html') 
    }
    else{
        const erroMsg = document.getElementById('error-msg')
        erroMsg.innerText = resultado[Object.keys(resultado)[0]]
        erroMsg.style.display = 'block'
    }
})