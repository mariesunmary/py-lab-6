def generate_square_set(n):
    square_set = {i ** 2 for i in range(1, n + 1)}
    return square_set

def main():
    try:
        n = int(input("Введіть кількість елементів множини: "))
        if n < 0:
            print("Будь ласка введіть тільки додатнє число.")
            return
        
        square_set = generate_square_set(n)
        
        print("Множина квадратів цілих чисел від 1 до 1000:")
        print(sorted(square_set))

    except ValueError:
        print("Помилка. Введіть ціле число.")

main()
