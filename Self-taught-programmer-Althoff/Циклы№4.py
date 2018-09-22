numbers = [11, 78, 90]
while True:
    answer = input("Угадайте число или введите X для выхода.")
    if answer == "X":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Пожалуйста, введите число или X для выхода.")
    if answer in numbers:
        print("Вы угадали!")
    else:
        print("Неправильно!")

       
            
