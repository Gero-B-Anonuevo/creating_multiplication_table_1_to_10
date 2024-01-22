first_number = 1

while first_number < 11:
    for num in range(11):
        num = first_number
        for num2 in range(11):
            num2 = first_number
            print(num, end='')
    print()
    first_number = first_number + 1