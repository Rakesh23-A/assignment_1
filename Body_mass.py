##BODY MASS

print("it is only for 20 years or older")

print("\n")

weight=float(input("enter your weight  [ in  pound ]  : "))

height=float(input("enter your height  [ in  inch ]  : "))

BMI=(weight*0.45359237)/(pow((height*0.0254),(1/2)))

if weight<=0 or height<=0:
    print("error")
    
else:
    if BMI<18.5:
        i="Underweight"
    elif BMI<25.5:
        i="Normal"
    elif BMI<30.0:
        i="Overweight"
    else:
        i="Obese"
    print("your status  :",i)
