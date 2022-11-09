from words import words
import random

br = ('-' * 40)

print(br)
print("Добро пожаловать в наш тренажёр!")
print("Сколько слов готовы перевести?:")
print(br)
answer = input()
answer = int(answer)
print("Ваш выбор: ", answer, "слов(а). Удачи!")

count = 0

for i in range(answer):

    word, key = random.choice(list(words.items()))

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
print("\nРабота программы завершена.\nЖелаю удачи!")
