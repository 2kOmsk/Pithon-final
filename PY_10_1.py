
words = ['разработка', 'сокет', 'декоратор']
for word in words:
    print(f"Слово '{word}' на те буквы:")
    for cell in word:
        print(cell, end=' ')
    print(f"\nТип: {type(word)}\n")

for word in words:
    print(f"Слово '{word}' точки в Unicode:")
    unicode_word = ''
    for cell in word:
        unicode_word += f"\\u{ord(cell):04x}"
    print(f"Тип : {type(unicode_word)}")
    print(f"Значение: {unicode_word}\n")
