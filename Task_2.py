with open("text_1.txt.", "r", encoding="utf-8") as t_1:
    content = t_1.readlines()
    lines = len(content)
    print(f"Amount of lines in your document is {lines}")
    l = 0
    for i in content:
        words = i.split(" ")
        words = len(words)
        l += 1
        print(f"Amount of words in line {l} is {words}")
