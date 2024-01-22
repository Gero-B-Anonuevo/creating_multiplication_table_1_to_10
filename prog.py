first_number = 1

while first_number < 10:
    for num in range(11):
        num = first_number
        print(num, end='')
    print()
    first_number = first_number + 1