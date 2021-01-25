def int_func():
    words = input("Enter words in small english letters using space between:")
    word_case = []
    for word in words.split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
                word_case.append(word.title()) if chars == len(word) else ""
    words_final = " ".join(word_case)
    return words_final


print(int_func())
