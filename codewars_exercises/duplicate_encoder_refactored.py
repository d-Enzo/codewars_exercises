def duplicate_encode(word):
    encoded_word = ""
    word = word.lower()
    for character in word:
        if word.count(character) > 1:
            encoded_word += ")"
        else:
            encoded_word += "("
    return encoded_word