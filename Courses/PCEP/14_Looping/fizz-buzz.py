values = int(input("How many values should we process: "))

values_range = range(1,values + 1)

for value in values_range:
    # print(value)
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
    elif value % 3 == 0:
        print("Fizz")
    elif value % 5 == 0:
        print("Buzz")
    else:
        print(value)