def anagram(x, y):
    print("Эта программа определяет, являются ли два слова анаграммами друг друга")
    x = input("Введите первое слово: ")
    y = input("Введите воторе слово: ")
    x = x.lower()
    y = y.lower()
    if not len(x) == len(y):
        print("Данные слова не являются анаграммами")
    else:
        if sorted(x) == sorted(y):
            print("Данные слова являются анаграммами")
        else:
            print("Данные слова не являются анаграммами")

anagram("dd", "qdq")