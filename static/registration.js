document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('usname').value;
    const password = document.getElementById('password').value;

    const data = { username: username, password: password };

    fetch('/registration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Пользователь добавлен');
        location.href = "/login";
    })
    .catch(error => {
        console.error('Error:', error);
    });
});