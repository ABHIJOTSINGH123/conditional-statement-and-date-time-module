height=float(input("enter your height cms"))
weight=float(input("enter your weight in kgs"))
BMI=weight/(height/100)**2
print("your BMI is ", BMI)
if BMI<=18.4:
    print("your are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=34.9:
    print("you are severly overweight")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are severly obese")
