document.addEventListener("DOMContentLoaded", () => {
    let timerElement = document.getElementById("timer");
    let totalTime = parseInt(timerElement.textContent.match(/\d+/)[0]);

    const interval = setInterval(() => {
        totalTime--;
        timerElement.textContent = `Осталось времени: ${totalTime} секунд`;

        if (totalTime <= 10) {
            timerElement.style.color = "red"; // Таймер становится красным
        }

        if (totalTime <= 0) {
            clearInterval(interval);
            document.getElementById("quizForm").submit();
        }
    }, 1000);
});
