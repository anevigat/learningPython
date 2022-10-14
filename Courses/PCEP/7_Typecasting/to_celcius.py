fahrenheit = input("What temperature (in Fahrenheit) would you like converted to Celsius?")
celsius = (float(fahrenheit) - 32) * 5 / 9

print(f"{round(float(fahrenheit), 2)} F is {round(celsius, 2)} C")