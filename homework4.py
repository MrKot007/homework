year = int(input('year '))
if year%1000 == 0:
    century = century = (year//100)
else:
    century = (year//100)+1
print(century)