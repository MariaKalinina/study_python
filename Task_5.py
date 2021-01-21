rating = [7, 4, 4, 3]
new_el = int(input("Add rating point from 0 to 9: "))
if new_el > max(rating):
    rating.insert(rating.index(max(rating)), new_el)
    print(rating)
elif new_el < min(rating):
    rating.insert(rating.index(min(rating))+1, new_el)
    print(rating)
elif new_el in rating:
    rating.insert((rating.index(new_el) + rating.count(new_el)), new_el)
    print(rating)
elif new_el not in rating and max(rating):
    rating.insert(0, new_el)       # Короткий вариант, если нет условия про постановку после повторов
    rating.sort(reverse=True)
    print(rating)
