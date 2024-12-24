document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault();
    
    const textarea = document.getElementById('e_t').value;

    const data = { message: textarea };
    fetch('/work', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        answer = data['generated_text'];
        new_element = document.getElementById('response');
        new_element.textContent = answer;
    });
});