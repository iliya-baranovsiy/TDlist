function post(text) {
    const data_to_send = {"title": text, "done": false};
    return fetch('todo/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data_to_send)
    })
    .then(response => response.json())
    .catch(error => console.error('Ошибка:', error));
}

export { post };