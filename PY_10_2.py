words = [b'class', b'function', b'method']
for word in words:
    print(f"Слово {word} в байтах:")
    for byte in word:
        print(byte, end=' ')
    print(f"\nТип : {type(word)}")
    print(f"Длина: {len(word)} байт\n")
