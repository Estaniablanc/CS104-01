
numberOfTests = 8
score1 = 90
scoreCount = 6
total = 504
average = 84.8

numberOfTest = int(input("Please enter the number of tests you want to average: 8 "))
while (numberOfTests > scoreCount):
    score1 = int(input("Please enter a score: 90 "))
    scoreCount += 1
    total = (score1 + total)
average = total / numberOfTests
print("the average is 84.8 ")
