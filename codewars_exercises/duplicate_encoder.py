def duplicate_encode(word):
    output = []
    encoded_word = ""
    word = word.lower()
    for character in word:
        if word.count(character) > 1:
            output.append(")")
        else:
            output.append("(")
    return encoded_word.join(output)