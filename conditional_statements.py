# This is an if statement
age = int(input("Enter your age\n"))
if age < 20:
    print("Sorry, you can't attend this party")
else:
    print("Welcome to the party")

# Simple interest calculator
principle = float(input("Enter your principle\n"))
rate = float(input("Enter your rate\n"))
time = float(input("Enter your time\n"))
simpleInterest = (principle * rate * time) / 100
if simpleInterest <= 1000:
    print("The loan is affordable")
elif simpleInterest <=2000:
    print("The loan is expensive")
else:
    print("This is a scam")