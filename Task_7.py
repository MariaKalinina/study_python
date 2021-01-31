import json

with open("text_7.txt.", "r", encoding="utf-8") as t_7:
    lines = t_7.readlines()
    all_companies = {}
    for li in lines:
        company = li.split()
        fin_res = int(company[2]) - int(company[3])
        all_companies[company[0]] = fin_res
    list_profit = []
    for i in list(all_companies.values()):
        if i > 0:
            list_profit.append(i)
    profit = sum(list_profit) / len(list_profit)
    profit_dict = {"average profit": profit}
    full = [all_companies, profit_dict]
    with open("task_7j.json", "w", encoding="utf-8") as j_7:
        json.dump(full, j_7, sort_keys=True, indent=4, ensure_ascii = False)
