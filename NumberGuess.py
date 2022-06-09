import random
import sys
print('Добро пожаловать в числовую угадайку')
print('Компьютер загадал число от 1 до 100')
choice_hum = input('Начать игру нажмите: Д/Н  ')
num_of_att = 0


def is_valid(x, bot):
    while True:
        if (x < 100) and (x > 0):
            wrong_right(x, bot)
        else:
            print('Введите число от 1 до 100')
            x = int(input())


def wrong_right(answer, bot):
    global choice_hum, num_of_att
    if answer > bot:
        print('Ваше число больше загаданного, попробуйте еще разок')
        num_of_att += 1
        replay_hum(bot)
    elif answer < bot:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        num_of_att += 1
        replay_hum(bot)
    elif answer == bot:
        print('Вы угадали, поздравляем!')
        print('Количество попыток', num_of_att)
        choice_hum_rep = input('Хотите попробовать ещё раз? Д/Н  ')
        human(choice_hum_rep)


def replay_hum(bot):
    int_hum = int(input())
    is_valid(int_hum, bot)


def human(choice_hum_play):
    while choice_hum_play == 'Д':
        print('Угадайте какое число загадал копьютер')
        bot = random.randint(1, 100)
        print(bot)
        int_hum = int(input())
        is_valid(int_hum, bot)
    else:
        print('До свидания')
        sys.exit()


human(choice_hum)
