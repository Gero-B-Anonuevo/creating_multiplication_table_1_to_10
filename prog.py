first_number = 1

while first_number < 11:
    for num in range(1):
        num = first_number
        for num2 in range(1, 11):
            print(num*num2, end=' ')
    print()
    first_number = first_number + 1