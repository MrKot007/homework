hours = int(input("hour: "))
minutes = int(input("minute: "))
seconds = int(input("second: "))

hours1 = int(input("hour: "))
minutes1 = int(input("minute: "))
seconds1 = int(input("second: "))

difference = (hours1*3600+minutes1*60+seconds1)-(hours*3600+minutes*60+seconds)
print(difference)