in_list = input("Enter several words using space between them: ")
word_list = in_list.split()
for ind, el in enumerate(word_list, 1):
    print(ind, el[:10])
