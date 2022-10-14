# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name

def split_name(name):
    return {"first_name": name.split()[0], "last_name": name.split()[1]}

assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names

def split_name(name):
    name_splited = name.split()
    if len(name_splited) == 2:
        return {"first_name": name.split()[0], "last_name": name.split()[1]}
    else:
        return {"first_name": name.split()[0], "last_name": ' '.join(name.split()[1::])}

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)

def is_palindrome(word):
    return word == word[::-1]

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers

def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list

def build_list(word, number=1):
    lista = []
    for _ in range(number):
        lista.append(word)
    return lista

assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
