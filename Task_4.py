with open("text_4.txt.", "r", encoding="utf-8") as t_4, open("text_4_w.txt.", "w", encoding="utf-8") as t_4w:
    lang_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for lines in t_4:
        trans = lang_dict.get(lines.split()[0])
        to_file = t_4w.writelines(f"{trans} {lines.split()[1]} {lines.split()[2]} \n")
