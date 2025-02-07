export function markAsDone(id) {
    const button = document.getElementById(`doneBtn-${id}`);
    button.disabled = true;
    button.innerText = 'Awesome';

    fetch(`/todo/${id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"done": true}),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}