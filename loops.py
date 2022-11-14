# LOOPS
# While loop
counter = 0
while counter <=5:
    print(counter)
    counter+=1

counterTwo = 90
while counterTwo >= 85:
    print(counterTwo)
    counterTwo-=1


counterThree = 20
while counterThree <= 50:
    if counterThree%2==1:
        print(counterThree)
    counterThree+=1




# For in loop
numbers = range(20,6,-1)
for nambari in numbers:
    print(nambari)

marks = range(40,101,10)
for mark in marks:
    if mark <= 40:
        print("E")
    elif mark<=50:
        print("D")
    elif mark <= 60:
        print("C")
    elif mark <= 70:
        print("B")
    else:
        print("A")