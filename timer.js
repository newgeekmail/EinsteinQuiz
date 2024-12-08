document.addEventListener("DOMContentLoaded", () => {
    let timerElement = document.getElementById("timer");
    let timeLeft = parseInt(timerElement.textContent.split(" ")[2]); // Получаем время

    const interval = setInterval(() => {
        timeLeft--;
        timerElement.textContent = `Осталось времени: ${timeLeft} секунд`;

        if (timeLeft <= 0) {
            clearInterval(interval);
            document.getElementById("quizForm").submit(); // Отправляем форму
        }
    }, 1000);
});
