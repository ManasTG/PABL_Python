#%% Task 1- print Hello world
print("Task 1- Print Hello World")
print("Hello World")


#%% Task 2- CV
print("\nTASK 2 - CV")
print("""CV
Name: Manas
Age: 19
Course: B.Tech - CSE
Languages: Python, C""")


#%% Task 3- Print Circumference
print("\nTASK 3- Circumference")
r = float(input("Enter the radius the Circle: "))
circ_circle = 2*r*3.14
print(f"The circumfrence of the circle is {circ_circle:.2f}")


#%% task 4- area of the circle
print("\nTASK 4- area of the circle")
area_circle = r*r*3.14
print(f"The area of of the circle is {area_circle:.2f}")


#%% task 5- Calculate the area of a triangle
print("\nTASK 5- Triangle Area")
height_triangle = float(input("Enter the Height of the Triangle: "))
base_triangle = float(input("Enter the Base of the Triangle: "))
area_of_Triangle = 0.5 * base_triangle * height_triangle

print(f"The Area of the Triangle is {area_of_Triangle:.2f}")


#%% task 6- Design simple interest calculator
print("\nTASK 6 - SI Calculator")
principle = float(input("Enter the Principle amount: "))
rate_of_intrest = float(input("Enter the Rate of Intrest: "))
time_intrest = float(input("Enter the Duration in the year: "))

simple_int = (principle * rate_of_intrest * time_intrest)/100
print(f"The Calculation of Simple Intrest is: {simple_int:.2f}")


#%% task 7- Design Celsius to Fahrenheit calculator °F = (°C × 1.8) + 32
print("\nTask 7- C to F Calculator")
celsius_input = float(input("Enter the value of the Temperatur in Celsius to convert in Fahrenheit: "))

temperatur_calc = (celsius_input*1.8) + 32
print(temperatur_calc)


#%% task 8- Avg of 3 numbers
print("\nTask 8- Avg of 3 Numbers")
n1 = float(input("Enter the First number: "))
n2 = float(input("Enter the Second number: "))
n3 = float(input("Enter the Third number: "))
print("The Average of the 3 numbers are: ", (n1+n2+n3)/3)


#%% task 9- Area of Rectangle
print("\nTask 9- Area of Rectangle")
length_rect = float(input("Enter the Length of the Rectangle: "))
bre_rect = float(input("Enter the Breath of the Rectangle: "))
print("The area of the Rectangle is: ", (length_rect * bre_rect))


#%% task 10- Age in Days
print("\nTask 10 - Age to Days")
age = int(input("Enter the age of the Person: "))
age_conv = age*365
print("The converted age is ", age_conv)
