const form = document.getElementById("textForm");
form.addEventListener("submit", logText);

function clearForm() {
            document.getElementById("textForm").reset(); // Очищаем форму
        }

function logText(event) {
    event.preventDefault();
    const textInput = document.getElementById("text_input").value;
    console.log("Введённый текст:", textInput);
    clearForm()
    // Если вы хотите, чтобы форма действительно отправлялась после логирования, можете раскомментировать следующую строку:
    // document.getElementById("textForm").submit();
}




