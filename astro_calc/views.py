from django.shortcuts import render
from datetime import datetime

# Словарь с описаниями знаков зодиака
ZODIAC_DESCRIPTIONS = {
    "Козерог": "Целеустремленный, ответственный и трудолюбивый. Всегда идет к своей цели.",
    "Водолей": "Креативный, свободолюбивый и оригинальный. Любит экспериментировать и искать новые пути.",
    "Рыбы": "Чувствительный, интуитивный и романтичный. Глубоко понимает эмоции окружающих.",
    "Овен": "Энергичный, решительный и смелый. Всегда готов к новым вызовам.",
    "Телец": "Практичный, надежный и терпеливый. Любит комфорт и стабильность.",
    "Близнецы": "Остроумный, общительный и любознательный. Легко находит общий язык с людьми.",
    "Рак": "Заботливый, эмоциональный и привязчивый. Ценит семью и уют.",
    "Лев": "Харизматичный, уверенный в себе и амбициозный. Любит быть в центре внимания.",
    "Дева": "Аналитичный, внимательный к деталям и трудолюбивый. Всегда стремится к совершенству.",
    "Весы": "Дипломатичный, гармоничный и справедливый. Стремится к балансу во всем.",
    "Скорпион": "Страстный, загадочный и целеустремленный. Обладает сильной волей.",
    "Стрелец": "Оптимистичный, свободолюбивый и жизнерадостный. Любит путешествия и приключения."
}

# Функция для определения знака зодиака
def get_zodiac_sign(day, month):
    zodiac_signs = [
        (1, 20, "Козерог"), (2, 19, "Водолей"), (3, 20, "Рыбы"),
        (4, 20, "Овен"), (5, 21, "Телец"), (6, 21, "Близнецы"),
        (7, 22, "Рак"), (8, 23, "Лев"), (9, 23, "Дева"),
        (10, 23, "Весы"), (11, 22, "Скорпион"), (12, 21, "Стрелец"),
        (12, 31, "Козерог")  # Для конца декабря
    ]

    for start_month, start_day, sign in zodiac_signs:
        if (month == start_month and day <= start_day) or (month < start_month):
            return sign
    return "Козерог"  # По умолчанию

# Основная вьюшка
def index(request):
    zodiac_sign = None
    description = None
    birthdate = request.GET.get("birthdate")

    if birthdate:
        date_obj = datetime.strptime(birthdate, "%Y-%m-%d")
        zodiac_sign = get_zodiac_sign(date_obj.day, date_obj.month)
        description = ZODIAC_DESCRIPTIONS.get(zodiac_sign, "Описание отсутствует.")

    return render(request, 'astro_calc/index.html', {
        "zodiac_sign": zodiac_sign,
        "description": description
    })
