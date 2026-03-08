def letter_positions_20(sentence):
    result = []
    for char in sentence.lower():
        if char.isalpha():
            pos = ord(char) - ord('a') + 1
            if pos > 20:
                pos -= 20
            result.append(pos)
    return result

while True:
    text = input("Enter a sentence (type 'exit' to quit): ")
    if text.lower() == "exit":
        break
    print(letter_positions_20(text))