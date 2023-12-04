def get_count(sentence):
    vowel_count = 0
    for character in sentence:
        if character == "a":
            vowel_count += 1
        if character == "e":
            vowel_count += 1
        if character == "i":
            vowel_count += 1
        if character == "o":
            vowel_count += 1
        if character == "u":
            vowel_count += 1
    return vowel_count