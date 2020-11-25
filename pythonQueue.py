x = 0
y = 0
total = 0


number = int(input("10"))
Names = ["Josh","Tosha","Melissa","Alicia","Maria","Angelica","Tom","Dan","Brianna","eevee"]
for Names in number > x:
    acceptedName = str(input("Josh","Tosha","Melissa","Alicia","Maria","Angelica","Tom","Dan","Brianna","eevee"))
    Names.append(acceptedName)
    x = x+1

total = len(Names)
while total > y:
    print (Names.pop(0))
    y = y+1
