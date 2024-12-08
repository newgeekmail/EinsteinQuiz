from flask import Flask, render_template, request

app = Flask(__name__)

# Вопросы и ответы
questions = [
    {
        "question": "Какое из следующих утверждений соответствует правилу 'Следуй своей любознательности'?",
        "options": [
            "Никогда не сдавайся, даже если не понимаешь что-то.",
            "Задавай вопросы о том, что вызывает интерес, и ищи ответы.",
            "Всегда следуй общественным стандартам успеха."
        ],
        "correct": 1
    },
    {
        "question": "Эйнштейн считал, что воображение важнее знаний. Почему?",
        "options": [
            "Потому что оно помогает учить школьные уроки быстрее.",
            "Воображение – это предварительный просмотр будущих событий.",
            "Знания всегда устаревают, а воображение вечно."
        ],
        "correct": 1
    },
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions, total_time=60)  # 60 секунд на тест

@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form
    score = 0
    for i, question in enumerate(questions):
        if int(answers.get(f"q{i}", -1)) == question["correct"]:
            score += 1
    return render_template("result.html", score=score, total=len(questions))

if __name__ == "__main__":
    app.run(debug=True)
