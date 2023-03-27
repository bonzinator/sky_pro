import json


# Функция считывает json файл, преобразует его в словарь python
def load_questions():
    with open('questions.json') as f:
        python_dict = json.load(f)
        return python_dict


python_dict2 = load_questions()


# Функция перебирает словарь полученный из функции load_questions() и выдает ключи
# словаря python_dict2 и ключи вложенного словаря в одну строку
def show_field(ex):
    for key, value in ex.items():
        print(key.ljust(20), end='')
        for price, data_u in value.items():
            asked = data_u["asked"]
            if not asked:
                print(price, end=' ')
            else:
                print("   ", end=' ')
        print()


# Функция принимает ввод пользователя, переводит его в словарь и возвращает его
def parse_input():
    user_var = input('Введите Тему и Стоимость: ')
    user_list = user_var.split()
    return user_list


# Функция перебирает значения и ключи в словаре с вопросами и ответами и выдает значение вопроса
def show_questions(theme, prise):
    for key, value in python_dict2.items():
        if key == theme:
            for i, j in value.items():
                if i == prise:
                    j["asked"] = True
                    return j["question"]


# Функция возвращает статистику игры
def show_result(a, b, c):
    print(f'У нас закончились вопросы!\n'
          f'Ваш счет: {a}\n'
          f'Верных ответов: {b}\n'
          f'Неверных ответов: {c}\n')


# Функция возвращает количество ответов
def len_dict(a):
    n = 0
    for i, j in a.items():
        for a in j:
            n += 1
    return n


# Функция возвращает измененную таблицу в новый json файл
def save_result_to_file(a, b, c):
    file = open("example.json", r)
    result = json.load(file)
    file.close()

    result.append({
        "points": a,
        "correct": b,
        "incorrect": c
    })

    file = open("example.json", "w")
    json.dump(result, file)
    file.close()


count = 0

points = 0
correct = 0
incorrect = 0

while points < len_dict(python_dict2):
    show_field(python_dict2)
    user_input = parse_input()  # Словарь с запросом пользователя
    show_questions(user_input[0], user_input[1])

    print(f'Слово {show_questions(user_input[0], user_input[1])} в переводе означает...')
    user_var = input('Введите ответ: ')

    for key, value in python_dict2.items():
        if key == user_input[0]:
            for i, j in value.items():
                if i == user_input[1]:
                    if user_var == j['answer']:
                        count += int(i)
                        print(f'Верно, + {i}. Ваш счет {count}!')
                        correct += 1
                        break

                    elif user_var != j['answer']:
                        count -= int(i)
                        print(f'Неверно, на самом деле {j["answer"]} - {i}. Ваш счет {count}!')
                        incorrect += 1
                        break

    points += 1

show_result(points, correct, incorrect)
save_result_to_file(points, correct, incorrect)
