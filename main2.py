import random

from words import words


def names():
    try:
        print("\nДобро пожаловать в наш тренажёр!\n")
        name = input("Как можно к вам обращаться?\n")
        name = name.capitalize()
        print(f"Привет, {name}!")
        change(name)
    except Exception as eror:
        print("Ошибка при знакомстве"), eror


def change(name):
    try:
        print(f"{name}, пора выбрать режим перевода)))")
        print("\nПереводим: \nс английского языка на русский - (1)\nс русского на английский - (2)")
        print("(((просто посмотреть словарь))) - (3)")
        ch = int(input())
        if (ch <= 0) or (ch > 3):
            print(f"{name}, выберите пожалуйста '1' или '2'!")
            change(name)
        elif ch == 3:
            show_to_dictionary(name)
        else:
            print("Ваш выбор,- ", ch)
            greeting(ch, name)
    except Exception as eror:
        print("Ошибка работы программы,", eror)


def show_to_dictionary(name):
    print("Показываю текущий словарь: \n")
    for k, v in words.items():
        print(f"\t{k} - {v}")
    print(f"\nХорошего дня, {name}!")


def greeting(ch, name):
    try:
        print(f"{name}, сколько слов готовы перевести?:")
        answer = int(input())
        if answer < 0:
            print("Введите пожалуйста положительное число.")
            greeting(ch, name)
        elif answer > 50:
            print("Слишком большое число\nЯ беспокоюсь о вас\nВведите пожалуйста меньшее число.")
            greeting(ch, name)
        else:
            print("Ваш выбор: ", answer, "слов(а). Удачи!")
            train(answer, ch, name)

    except Exception as eror:
        print("Работа программы вызвала ошибку:", eror)


def train(answer, ch, name):
    try:
        word, key = [], []
        count = 0
        for i in range(answer):
            if ch == 1:
                word, key = random.choice(list(words.items()))
            elif ch == 2:
                key, word = random.choice(list(words.items()))

            print("\nВведите перевод слова -", word)
            ans_word = input()
            ans_word = str.lower(ans_word)

            if ans_word == key:
                count += 1
                print("Вы правы, ответом на слово -", word, "будет ", key)
                print("Правильно переведено -", count, " слов(а)")
            else:
                print("К сожалению вы ошиблись, и переводом слова -", word, "станет -", key)
                print("Вы ввели правилный перевод -", count, " слов(а)")

        print("\nПоздравляю, вы перевели ", count, " слов из ", answer)
        if count == answer:
            print("И ваш результат впечатляет!")
        elif count == answer - 1:
            print("Очень даже хорошо! Но уверен,- вы сможете и лучше!")
        else:
            print("Что ж, неплохо! Но вам есть куда расти)")

    except Exception as eror:
        print("Работа программы прервана ошибкой ", eror)
    finally:
        print(f"\n{name}, Работа программы успешно завершена, удачи!")


names()
input("\n\nДля выхода из программы нажмите клавишу (Ввод)")
