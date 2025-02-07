function change(id, text) {
    let data_to_send = { "title": text };
    return fetch(`/todo/${id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data_to_send)
    })
    .then(response => {
        if (response.ok) {
            if (response.status === 204) {
                console.log('Task deleted successfully, no content returned');
                return null;
            } else {
                return response.json();
            }
        } else {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    })
    .then(data => {
        if (data) {
            console.log('Success:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

export { change };