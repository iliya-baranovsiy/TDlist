import { change } from "./change.js";
document.querySelectorAll('.change-button').forEach(button => {
    button.addEventListener('click', function() {
        const todoId = this.dataset.todoId;
        const todoText = this.closest('.todo-item').querySelector('p').textContent;

        document.getElementById('changeInput').value = todoText;

        document.getElementById('popup-overlay').style.display = 'block';
        document.getElementById('popup').style.display = 'block';

        const changeForm = document.getElementById('changeForm');
        changeForm.onsubmit = function(event) {
            event.preventDefault();
            change(todoId, changeInput.value).then(() => {
                closePopup();
                location.reload();
            });
        };
    });
});

document.querySelector('.close-popup').addEventListener('click', closePopup);

function closePopup() {
    document.getElementById('popup-overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
    document.getElementById('changeInput').value = '';
}