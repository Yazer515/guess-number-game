import random

print("Добро пожаловать в игру \"Угадай число\"!"
      "\nЦель игры состоит в том, что пользователю необходимо угадать загаданное компьютером число"
      "\nДля начала необходимо ввести максимальное число, которое может загадать компьютер"
      "\nПо умолчанию минимальное значение равно 0, а максимально возможное от 2 до 100")

min_value = 0

def check_max_value():
    while True:
        max_value = input("Введите максимальное число: ")
        if not max_value.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        elif not min_value < int(max_value) <= 100:
            print("Ваше число не диапазоне. Попробуйте снова")
        else:
            max_value = int(max_value)
            return max_value
            break

def check_find_value():
    while True:
        input_value = input("Введите число: ")
        if not input_value.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        elif not min_value <= int(input_value) <= max_value:
            print("Ваше число не диапазоне. Попробуйте снова")
        else:
            input_value = int(input_value)
            return input_value
            break


max_value = check_max_value()

find_value = random.randint(min_value, max_value)

print("\033[32mТеперь попробуйте ввести загаданное компьютером число :)\033[0m")

attempt = 0

while True:
    check_value = check_find_value()
    if check_value == find_value:
        print("\033[32mВы угадали загаданное число " + str(find_value) + "! Попыток: " + str(attempt))
        break
    elif check_value > find_value:
        attempt += 1
        print("\033[31mМного! Попыток: " + str(attempt)+"\033[0m")
    elif check_value < find_value:
        attempt += 1
        print("\033[31mМало! Попыток: " + str(attempt)+"\033[0m")

