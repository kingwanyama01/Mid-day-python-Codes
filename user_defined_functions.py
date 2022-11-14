def motto():
    print("Hello this is our motto. Thank you.")

motto()


def addition():
    answer = 10 + 20
    print("Your answer is",answer)
addition()

def sum(x,y,z):
    answer = x + y + z
    print("Hello your answer is",answer)
sum(323232,7558878,876758)
sum(32,54,87)

def avg(x,y,z):
    average = (x + y + z) / 3
    return average

myValue = avg(323,545,7676)
print(myValue)

# Create a function to calculate the BMI of any person.
# Use formula BMI = weight divided by height squared
# Chjeck and ascertain that if:
    # BMI < 24 ------------------- Underweight
    # BMI < 29 ------------------- Normal weight
    # BMI < 34 ------------------- Overweight
    # else ------------------- Obese

def bmi(w,h):
    bmi = w/pow(h,2)
    if bmi < 24:
        print(bmi,"Underweight")
    elif bmi < 29:
        print(bmi,"Normal weight")
    elif bmi < 34:
        print(bmi,"Overweight")
    else:
        print(bmi,"Obese")
bmi(180,24)



