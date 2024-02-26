def add_element(list):
    left_element = input("Введіть елемент для додавання зліва: ")
    list.insert(0, left_element)
    right_element = input("Введіть елемент для додавання справа: ")
    list.append(right_element)

    return list

list = []

# Ввід списку 
lenght = int(input("Введіть довжину списку: "))
for _ in range(lenght):
    element = input("Введіть елемент списку: ")
    list.append(element)

# Додавання елементів до списку з обох кінців
new_list = add_element(list)

# Вивід оновленого списку
print("Оновлений список:", new_list)
