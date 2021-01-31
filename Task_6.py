with open("text_6.txt", "r", encoding="utf-8") as t_6:
    all_dis = t_6.readlines()
    dis_dict = {}
for line in all_dis:
    discipline = line.split()
    dis_hours = []
    for character in line:
        symbols = '1234567890 '
        if character in symbols:
            dis_hours.append(character)
            hours_str = "".join(dis_hours)
            total_hours = sum(map(int, hours_str.split()))
            dis_dict[discipline[0][:-1]] = total_hours
print(dis_dict)
