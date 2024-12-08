from flask import Flask, render_template, request, redirect, url_for
import logging  # Импорт модуля logging
from datetime import datetime

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    filename="test_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

questions = [
    # Множественный выбор (Multiple Choice)
    {
        "type": "multiple_choice",
        "question": "Пример вопроса множественного выбора: Что является важной чертой для достижения успеха?",
        "options": ["Сила", "Любознательность", "Богатство", "Соблюдение правил"],
        "correct": 1,
        "explanation": "Любознательность позволяет задавать правильные вопросы и искать ответы."
    },
    {
    "type": "multiple_choice",
    "question": "Что означает быть настойчивым?",
    "options": ["Избегать сложностей", "Придерживаться своих целей", "Игнорировать советы", "Следовать чужим инструкциям"],
    "correct": 1,
    "explanation": "Настойчивость помогает преодолевать трудности и достигать целей."
    },
    {
    "type": "multiple_choice",
    "question": "Как воображение может помочь в решении задач?",
    "options": ["Оно создаёт шаблоны", "Оно упрощает рутину", "Оно предлагает уникальные идеи", "Оно исключает ошибки"],
    "correct": 2,
    "explanation": "Воображение открывает новые пути и решения."
    },
    {
    "type": "multiple_choice",
    "question": "Почему ошибки важны для роста?",
    "options": ["Они показывают слабые стороны", "Они делают нас сильнее", "Они отвлекают от целей", "Они не имеют значения"],
    "correct": 0,
    "explanation": "Ошибки помогают выявить области для улучшения."
    },
    {
    "type": "multiple_choice",
    "question": "Как можно развить свои способности?",
    "options": ["Изучая новое", "Игнорируя сложности", "Повторяя чужие идеи", "Следуя рутине"],
    "correct": 0,
    "explanation": "Изучение нового развивает навыки и открывает перспективы."
    },
    {
    "type": "multiple_choice",
    "question": "Что делает работа творческой?",
    "options": ["Точное следование инструкциям", "Создание чего-то уникального", "Быстрое выполнение задач", "Избежание ошибок"],
    "correct": 1,
    "explanation": "Творческая работа включает создание уникальных решений."
    },
    {
    "type": "multiple_choice",
    "question": "Почему важно задавать вопросы?",
    "options": ["Это раздражает других", "Это показывает интерес", "Это уменьшает ошибки", "Это не имеет значения"],
    "correct": 1,
    "explanation": "Вопросы помогают лучше понять и учиться."
    },
    {
    "type": "multiple_choice",
    "question": "Что означает 'воображение важнее знаний'?",
    "options": ["Воображение заменяет знания", "Воображение открывает будущее", "Знания бесполезны", "Воображение создаёт рутину"],
    "correct": 1,
    "explanation": "Эйнштейн считал, что воображение позволяет увидеть возможности, которые ещё не реализованы."
    },
    {
    "type": "multiple_choice",
    "question": "Как справляться с неудачами?",
    "options": ["Избегать новых попыток", "Анализировать причины", "Обвинять других", "Забывать о них"],
    "correct": 1,
    "explanation": "Анализ ошибок помогает найти способы избежать их в будущем."
    },
    {
    "type": "multiple_choice",
    "question": "Почему важно думать самостоятельно?",
    "options": ["Это делает уникальным", "Это помогает копировать других", "Это снижает ответственность", "Это вызывает меньше вопросов"],
    "correct": 0,
    "explanation": "Самостоятельное мышление способствует созданию уникальных решений."
    },
    {
    "type": "multiple_choice",
    "question": "Что помогает развивать творческое мышление?",
    "options": ["Следование рутине", "Воображение", "Избежание сложностей", "Подражание другим"],
    "correct": 1,
    "explanation": "Воображение — ключ к созданию новых идей."
    },
    {
    "type": "multiple_choice",
    "question": "Что делает задачу интересной?",
    "options": ["Её простота", "Её сложность", "Её уникальность", "Её завершённость"],
    "correct": 2,
    "explanation": "Уникальность задачи вызывает интерес и вдохновляет."
    },
    {
    "type": "multiple_choice",
    "question": "Какой подход помогает в решении задач?",
    "options": ["Избегание ответственности", "Использование воображения", "Игнорирование ошибок", "Сравнение с другими"],
    "correct": 1,
    "explanation": "Воображение открывает новые пути для решения проблем."
    },
    {
    "type": "multiple_choice",
    "question": "Что делает обсуждение идей полезным?",
    "options": ["Подражание чужим решениям", "Обмен мыслями и аргументами", "Согласие со всеми", "Отказ от собственной точки зрения"],
    "correct": 1,
    "explanation": "Обсуждение идей помогает находить лучшие решения."
    },
    {
    "type": "multiple_choice",
    "question": "Как Эйнштейн определял успех?",
    "options": ["Через богатство", "Через достижения и идеи", "Через признание других", "Через избегание сложностей"],
    "correct": 1,
    "explanation": "Эйнштейн считал, что успех определяется вкладом в общество через идеи и открытия."
    },
    # Добавьте ещё 14 вопросов множественного выбора здесь

    # Сопоставление (Matching)
    {
        "type": "matching",
        "question": "Пример вопроса на сопоставление: Сопоставьте качества с их значением.",
        "pairs": {
            "Любознательность": "Способность задавать вопросы",
            "Настойчивость": "Умение преодолевать трудности",
            "Воображение": "Создание новых идей"
        },
        "correct": {
            "Любознательность": "Способность задавать вопросы",
            "Настойчивость": "Умение преодолевать трудности",
            "Воображение": "Создание новых идей"
        }
    },
    {
    "type": "matching",
    "question": "Сопоставьте утверждения и принципы.",
    "pairs": {
        "Учись на ошибках": "Анализируй свои действия.",
        "Воображение важнее знаний": "Мечтай о будущем.",
        "Любознательность": "Задавай вопросы и ищи ответы."
    },
    "correct": {
        "Учись на ошибках": "Анализируй свои действия.",
        "Воображение важнее знаний": "Мечтай о будущем.",
        "Любознательность": "Задавай вопросы и ищи ответы."
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте примеры с принципами.",
    "pairs": {
        "Придумывание нового изобретения": "Воображение важнее знаний",
        "Решение сложной задачи": "Будь настойчив",
        "Постановка вопросов на уроке": "Любознательность"
    },
    "correct": {
        "Придумывание нового изобретения": "Воображение важнее знаний",
        "Решение сложной задачи": "Будь настойчив",
        "Постановка вопросов на уроке": "Любознательность"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте качества с их описанием.",
    "pairs": {
        "Любознательность": "Стремление узнавать новое",
        "Настойчивость": "Продолжать, несмотря на трудности",
        "Творчество": "Создание уникальных идей"
    },
    "correct": {
        "Любознательность": "Стремление узнавать новое",
        "Настойчивость": "Продолжать, несмотря на трудности",
        "Творчество": "Создание уникальных идей"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте действия с их результатами.",
    "pairs": {
        "Анализ ошибок": "Улучшение навыков",
        "Использование воображения": "Создание новых идей",
        "Задавание вопросов": "Поиск ответов"
    },
    "correct": {
        "Анализ ошибок": "Улучшение навыков",
        "Использование воображения": "Создание новых идей",
        "Задавание вопросов": "Поиск ответов"
                }
    },
    {
    "type": "matching",
    "question": "Сопоставьте ситуации с их описанием.",
    "pairs": {
        "Исправление ошибок в проекте": "Учись на ошибках",
        "Придумывание инновационного решения": "Воображение важнее знаний",
        "Изучение новых областей": "Любознательность"
        },
    "correct": {
        "Исправление ошибок в проекте": "Учись на ошибках",
        "Придумывание инновационного решения": "Воображение важнее знаний",
        "Изучение новых областей": "Любознательность"
        }
    },
    {
    "type": "matching",
    "question": "Сопоставьте принципы с их результатами.",
    "pairs": {
        "Любознательность": "Поиск новых знаний",
        "Воображение": "Создание новых идей",
        "Настойчивость": "Достижение сложных целей"
    },
    "correct": {
        "Любознательность": "Поиск новых знаний",
        "Воображение": "Создание новых идей",
        "Настойчивость": "Достижение сложных целей"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте проблемы с их решениями.",
    "pairs": {
        "Сложная задача": "Будь настойчив",
        "Неизвестная область": "Задавай вопросы",
        "Творческий тупик": "Используй воображение"
    },
    "correct": {
        "Сложная задача": "Будь настойчив",
        "Неизвестная область": "Задавай вопросы",
        "Творческий тупик": "Используй воображение"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте утверждения с их примерами.",
    "pairs": {
        "Учись на ошибках": "Исправление неправильного расчёта",
        "Любознательность": "Изучение новой темы",
        "Воображение важнее знаний": "Придумывание уникального решения"
    },
    "correct": {
        "Учись на ошибках": "Исправление неправильного расчёта",
        "Любознательность": "Изучение новой темы",
        "Воображение важнее знаний": "Придумывание уникального решения"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте действия с их описанием.",
    "pairs": {
        "Проверка гипотезы": "Любознательность",
        "Творческое решение задачи": "Воображение важнее знаний",
        "Достижение результата через усилия": "Настойчивость"
    },
    "correct": {
        "Проверка гипотезы": "Любознательность",
        "Творческое решение задачи": "Воображение важнее знаний",
        "Достижение результата через усилия": "Настойчивость"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте задачи с их решениями.",
    "pairs": {
        "Трудная задача": "Будь настойчив",
        "Поиск нового метода": "Воображение важнее знаний",
        "Непонятный вопрос": "Задавай вопросы"
    },
    "correct": {
        "Трудная задача": "Будь настойчив",
        "Поиск нового метода": "Воображение важнее знаний",
        "Непонятный вопрос": "Задавай вопросы"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте ценности с их применением.",
    "pairs": {
        "Любознательность": "Изучение новой книги",
        "Настойчивость": "Продолжение работы несмотря на ошибки",
        "Воображение": "Создание уникального проекта"
    },
    "correct": {
        "Любознательность": "Изучение новой книги",
        "Настойчивость": "Продолжение работы несмотря на ошибки",
        "Воображение": "Создание уникального проекта"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте принципы с их примером.",
    "pairs": {
        "Учись на ошибках": "Анализ прошлого опыта",
        "Будь настойчив": "Решение сложной задачи",
        "Используй воображение": "Предложение новой идеи"
    },
    "correct": {
        "Учись на ошибках": "Анализ прошлого опыта",
        "Будь настойчив": "Решение сложной задачи",
        "Используй воображение": "Предложение новой идеи"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте задачи с их результатами.",
    "pairs": {
        "Изучение новой теории": "Любознательность",
        "Поиск нестандартного подхода": "Воображение важнее знаний",
        "Решение сложной задачи": "Будь настойчив"
    },
    "correct": {
        "Изучение новой теории": "Любознательность",
        "Поиск нестандартного подхода": "Воображение важнее знаний",
        "Решение сложной задачи": "Будь настойчив"
    }
    },
    {
    "type": "matching",
    "question": "Сопоставьте проблемы с их решениями.",
    "pairs": {
        "Неудача": "Учись на ошибках",
        "Нестандартная ситуация": "Используй воображение",
        "Долгая задача": "Будь настойчив"
    },
    "correct": {
        "Неудача": "Учись на ошибках",
        "Нестандартная ситуация": "Используй воображение",
        "Долгая задача": "Будь настойчив"
    }
    },    # Добавьте ещё 14 вопросов на сопоставление здесь
]

# Хранилище для имени пользователя
user_data = {"name": ""}

@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            return render_template("start.html", error="Введите ваше имя.")
        user_data["name"] = name
        return redirect(url_for("home"))
    return render_template("start.html")

@app.route("/test")
def home():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form
    score = 0
    feedback = []
    incorrect_answers = []

    for i, question in enumerate(questions):
        if question["type"] == "multiple_choice":
            user_answer = int(answers.get(f"q{i}", -1))
            if user_answer == question["correct"]:
                score += 1
            else:
                incorrect_answers.append({
                    "question": question["question"],
                    "your_answer": question["options"][user_answer] if user_answer != -1 else "Не отвечено",
                    "correct_answer": question["options"][question["correct"]]
                })
            feedback.append({
                "question": question["question"],
                "correct": question["options"][question["correct"]],
                "explanation": question["explanation"]
            })

    # Логирование результатов
    logging.info(
        f"Имя: {user_data['name']}, Итог: {score}/{len(questions)}, Неправильные ответы: {len(incorrect_answers)}, Детали: {incorrect_answers}"
    )

    return render_template("result.html", score=score, total=len(questions), feedback=feedback, incorrect_answers=incorrect_answers)

if __name__ == "__main__":
    app.run(debug=True)
