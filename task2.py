def delete_duplicates(input_list):
    new_list = []
    for element in input_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

def main():
    user_input = input("Введіть список через пробіл: ").split()

    new_list = delete_duplicates(user_input)

    print("Оновлений список без повторів:", new_list)

main()

