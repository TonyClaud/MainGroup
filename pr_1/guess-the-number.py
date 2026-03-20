import random

while True:
    print('---------------Угадай число---------------')

    print('''Выберите уровень сложности
    1.Легкий (1-50, 10 попыток)
    2.Средний (1-100, 7 попыток)
    3.Сложный (1-500, 5 попыток)''')

    while True:
        try:
            game_difficulty = int(input(''))
            if 1 <= game_difficulty <= 3:
                break
            else:
                print('Число должно быть от 1 до 3!')
        except ValueError:
            print('Введите цифру 1, 2 или 3!')

    print('Отлично! Начнем игру... Я загадал число...')
    print('------------Введите число-----------------')

    attempts = 0
    hidden_number = 0

    if game_difficulty == 1:
        attempts = 10
        hidden_number = random.randint(1, 50)
        max_num = 50
    elif game_difficulty == 2:
        attempts = 7
        hidden_number = random.randint(1, 100)
        max_num = 100
    elif game_difficulty == 3:
        attempts = 5
        hidden_number = random.randint(1, 500)
        max_num = 500

    progress = 1


    while True:
        while True:
            try:
                player_number = int(input())
                if 1 <= player_number <= max_num:
                    break
                else:
                    print(f'Число должно быть от 1 до {max_num}!')
            except ValueError:
                print('Введите целое число!')

        if player_number > hidden_number:
            print(f'Меньше, осталось {attempts - progress} попыток')
        elif player_number < hidden_number:
            print(f'Больше, осталось {attempts - progress} попыток')
        else:
            print(f'Верно! Я загадал {hidden_number}, '
                  f'ты угадал его за {progress} попыток')
            break

        if progress >= attempts:
            print(f'Попытки закончились! Ты проиграл. '
                  f'Я загадал число {hidden_number}')
            break

        progress += 1

    while True:
        print('Хочешь начать заново? Да/Нет')
        choice = input()
        if choice == 'Да' or choice == 'Нет':
            break
        else:
            print('Введите Да или Нет')

    if choice == 'Нет':
        print('Спасибо за игру! Всего хорошего')
        break