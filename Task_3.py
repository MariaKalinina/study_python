t_3 = open("text_3.txt.", "r", encoding="utf-8")
w_d_a = {}
for lines in t_3:
    worker = lines.split()
    w_d_a[worker[0]] = float(worker[1])
average_salary = sum(w_d_a.values()) / len(w_d_a)
print(f"Average salary of workers in the company = {average_salary}")
print("Employers who get less than 20000:  ")
for name, salary in w_d_a.items():
    if salary < 20000:
        print(name)
t_3.close()
