import { post } from "./post.js";

const form = document.getElementById("textForm");
form.addEventListener("submit", logText);

function clearForm() {
    document.getElementById("textForm").reset(); // Очищаем форму
}

function logText(event) {
    event.preventDefault();
    const textInput = document.getElementById("text_input").value;
    post(textInput).then(() => {
        location.reload();
    });
    clearForm();
}




