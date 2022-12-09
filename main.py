w1 = input("Введіть перше слово: ")
w2 = input("Введіть друге слово: ")

try:
    file = open("text.txt",encoding='utf8')
    text = file.read()

    result = text.replace(w1, w2)
    print(result)

