# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# 1) Преобразуйте его в дату в текущем году.
# 2) Логируйте ошибки, если текст не соответсвует формату.
# 3) Добавьте возможность запуска из командной строки.
# 4) При этом значение любого параметра можно опустить. 
#    В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# 5) Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

import argparse
import datetime

def parse_date(text_date):
    weekdays = {
        'понедельник': 0, 'пн': 0,
        'вторник': 1, 'вт': 1,
        'среда': 2, 'ср': 2,
        'четверг': 3, 'чт': 3,
        'пятница': 4, 'пт': 4,
        'суббота': 5, 'сб': 5,
        'воскресенье': 6, 'вс': 6
    }

    months = {
        'января': 1, 'янв': 1, '1': 1,
        'февраля': 2, 'фев': 2, '2': 2,
        'марта': 3, 'мар': 3, '3': 3,
        'апреля': 4, 'апр': 4, '4': 4,
        'мая': 5, '5': 5,
        'июня': 6, 'июнь': 6, 'июн': 6, '6': 6,
        'июля': 7, 'июль': 7, 'июл': 7, '7': 7,
        'августа': 8, 'авг': 8, '8': 8,
        'сентября': 9, 'сен': 9, '9': 9,
        'октября': 10, 'окт': 10, '10': 10,
        'ноября': 11, 'ноя': 11, '11': 11,
        'декабря': 12, 'дек': 12, '12': 12
    }

    current_year = datetime.date.today().year

    try:
        parts = text_date.split()
        if len(parts) >= 2:
            day_text = parts[0]
            day = int(day_text[:-2]) if day_text[:-2].isdigit() else 1

            weekday_text = parts[1].lower()
            weekday = weekdays.get(weekday_text, None)

            month_text = parts[2].lower()
            month = months.get(month_text, None)

            if None in (weekday, month):
                raise ValueError("Некорректные значения для дня недели или месяца.")

            date = datetime.date(current_year, month, 1)
            while date.weekday() != weekday:
                date += datetime.timedelta(days=1)
            date += datetime.timedelta(weeks=day - 1)

            return date

    except Exception as e:
        print(f"Ошибка: {e}")

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text_date", type=str, help="Текстовое представление даты")
    args = parser.parse_args()

    if args.text_date:
        user_input = args.text_date
    else:
        user_input = input("Введите текстовое представление даты: ")

    result_date = parse_date(user_input)
    if result_date:
        print(f"Результат: {result_date.strftime('%d.%m.%Y')}")