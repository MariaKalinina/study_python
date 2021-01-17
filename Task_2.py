time = int(input("Введите время в секундах: "))
time_hours = time // 3600
sec_left = time % 3600
time_min = sec_left // 60
tim_sec = sec_left % 60
print()
print(f"Время в формате чч:мм:сс - {time_hours:02}:{time_min:02}:{tim_sec:02}")
