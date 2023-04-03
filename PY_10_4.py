words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    encoded_word = word.encode('utf-8')
    decoded_word = encoded_word.decode('utf-8')
    print(f"Слово: {word}\nв байтах: {encoded_word}\nреверс: {decoded_word}\n")
