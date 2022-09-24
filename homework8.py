num = int(input('number '))
first_digit = num//100
second_digit = (num%100)//10
third_digit = num%10
if first_digit < second_digit and second_digit < third_digit:
    print('Да')
else:
    print('Нет')