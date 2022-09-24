n = int(input('days '))
today = 4
for i in range(1,n):
    today+=1
    if today == 6:
        today = 0
print(today)