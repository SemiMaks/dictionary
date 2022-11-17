from words import words
import random

print("Добро пожаловать в наш тренажёр!")


def change():
    try:
        print(
            "Выберите режим перевода.\nПереводим с английского языка на русский (1) или с русского на английский (2):")
        ch = int(input())
        if (ch <= 0) or (ch > 2):
            print("Выберите пожалуйста '1' или '2'!")
            change()
        else:
            print("Ваш выбор,- ", ch)
            greeting(ch)
    except Exception as eror:
        print("Ошибка работы программы,", eror)


def greeting(ch):
    try:
        print("Сколько слов готовы перевести?:")
        answer = int(input())
        if answer < 0:
            print("Введите пожалуйста положительное число.")
            greeting(ch)
        elif answer > 50:
            print("Слишком большое число\nЯ беспокоюсь о вас\nВведите пожалуйста меньшее число.")
            greeting(ch)
        else:
            print("Ваш выбор: ", answer, "слов(а). Удачи!")
            train(answer, ch)

    except Exception as eror:
        print("Работа программы вызвала ошибку:", eror)


def train(answer, ch):
    try:
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
                print("Вы ввели правилный перевод -", count, " слов")

        print("\nПоздравляю, вы перевели ", count, " слов из ", answer)

    except Exception as eror:
        print("Работа программы прервана ошибкой ", eror)
    finally:
        print("Работа программы успешно завершена, удачи!")


change()
