document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('usname').value;
    const password = document.getElementById('password').value;

    const data = { username: username, password: password }

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);  // Показываем ошибку
        } else {
            location.href = "/account";  // Переходим на страницу аккаунта
        }
    })
})