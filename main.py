word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

try:
    file = open("text.txt",encoding='utf8')
    text = file.read()

    result = text.replace(word1, word22)
    print(result)

