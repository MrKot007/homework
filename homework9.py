first_day = int(input('day1 '))
km_total = int(input('total '))
days = 1
while first_day <= km_total:
    first_day = first_day * 1.1
    days += 1
print(days)