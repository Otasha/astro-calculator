from django.shortcuts import render
from datetime import datetime


def calculate_pythagorean_square(birthdate):
    """Функция для расчета квадрата Пифагора"""
    digits = [int(digit) for digit in birthdate if digit.isdigit()]

    # Первое суммирование
    sum1 = sum(digits)
    sum1_digits = [int(digit) for digit in str(sum1)]

    # Второе суммирование (если сумма больше 9)
    sum2 = sum(sum1_digits)

    # Третье число — разница между первой и удвоенной первой цифрой
    if len(str(sum1)) > 1:
        sum3 = sum1 - 2 * int(str(sum1)[0])
    else:
        sum3 = sum1

    # Подсчет количества цифр в психоматрице
    all_digits = digits + sum1_digits + [sum2] + ([sum3] if sum3 > 0 else [])
    count_digits = {str(i): all_digits.count(i) for i in range(1, 10)}

    return count_digits


def pythagorean_square_view(request):
    """Обрабатывает запрос и отображает результат"""
    result = None
    birthdate = request.GET.get('birthdate')

    if birthdate:
        try:
            # Проверяем корректность даты
            datetime.strptime(birthdate, '%d-%m-%Y')
            result = calculate_pythagorean_square(birthdate)
        except ValueError:
            result = "Ошибка! Неверный формат даты. Введите в формате ДД-ММ-ГГГГ."

    return render(request, 'numerology/result.html', {'result': result})

