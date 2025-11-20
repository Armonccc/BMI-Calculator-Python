weight_pound = input("Please Enter your weight in pounds: ")

height_inch = input("Please Enter your height in inches: ")

meters_per_inch = 0.0254

weight_per_kilograms = 0.45359237



height_meter = height_inch * meters_per_inch

weight_meter = weight_pound * weight_per_kilograms

bmi = weight_meter / (height_meter * height_meter)

if bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print ("Normal")
elif bmi < 30:
    print ("Overweight")
else:
    print("Obese")







