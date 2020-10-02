temp = 0
x = 0
while x == 0:
    temp = int(input("please enter the current temperature "))
    if temp == 900:
        x = x+1
    if temp > 90:
        print("wear shorts")
    if temp > 70:
        print("short sleeves are fine")
    if temp > 50:
        print("wear a jacket")
    if temp > 32:
        print("wear a heavy coat")
    else:
        print("stay inside")
