import random

from words import words


def main():
    """Основная функция программы"""
    try:
        name = names()
        ch = change(name)
        answer = number_of_words(name)
        train(answer, ch, name)
    except Exception as eror:
        print("Ошибка при вызове функции знакомства"), eror


def names():
    """Функция возвращает имя пользователя"""
    try:
        print("\nДобро пожаловать в наш тренажёр!")
        name = input("Как можно к вам обращаться?\n")
        name = name.capitalize()
        print(f"Привет, {name}!")
        return name
    except Exception as eror:
        print("Ошибка при знакомстве"), eror


def change(name):
    """Функция возвращает выбор режима пользователя"""
    try:
        print("Что ж, пора выбрать режим перевода!")
        print("\nПереводим: \nс английского языка на русский - (1)\nс русского на английский - (2)")
        print("(((просто посмотреть словарь))) - (3)")
        ch = int(input())
        if (ch <= 0) or (ch > 3):
            print("Выберите пожалуйста '1', '2' или '3'!")
            change(name)
        elif ch == 3:
            show_to_dictionary(name)
        else:
            print(f"{name}, ваш выбор - ", ch)
            return ch
    except Exception as eror:
        print("Ошибка работы программы,", eror)


def show_to_dictionary(name):
    """Функция показывает словарь"""
    print("Показываю текущий словарь: \n")
    for k, v in words.items():
        print(f"\t{k} - {v}")
    print(f"\nХорошего дня, {name}!")
    input("\nДля завершения работы программы нажмите клавишу (Ввод)")
    exit()


def number_of_words(name):
    """Функция возвращает количество слов для перевода"""
    try:
        print(f"Сколько слов готовы перевести?:")
        answer = int(input())
        if answer < 0:
            print("Введите пожалуйста положительное число.")
            number_of_words(name)
        elif answer == 0:
            print("Введите пожалуйста больше 0.")
            number_of_words(name)
        elif answer > 50:
            print("Слишком большое число, я беспокоюсь о вас\nВведите пожалуйста меньшее число.")
            number_of_words(name)
        else:
            print("Ваш выбор: ", answer, "слов(а). Удачи!")
            answer = int(answer)
            return answer
    except Exception as eror:
        print("Работа программы вызвала ошибку:", eror)


def train(answer, ch, name):
    """Функция проверяет перевод пользователя"""
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

        print("\nВы перевели ", count, " слов из ", answer)
        if count == answer:
            print(f"{name}, поздравляю, ваш результат впечатляет!")
        elif count == answer - 1:
            print(f"{name}, очень даже хорошо! Но уверен,- вы сможете и лучше!")
        else:
            print(f"{name}, что ж, неплохо! Но вам есть куда расти)")

    except Exception as eror:
        print("Работа программы прервана ошибкой ", eror)
    finally:
        print(f"\n{name}, работа программы успешно завершена, удачи!")


if __name__ == "__main__":
    main()
    input("\n\nДля выхода из программы нажмите клавишу (Ввод)")
