#On the Twelfth day of Christmas,
#My true love gave to me:
#Twelve drummers drumming
#Eleven pipers piping
#Ten lords a-leaping
#Nine ladies dancing
#Eight maids a-milking
#Seven swans a-swimming
#Six geese a-laying
#Five golden rings
#Four calling birds
#Three french hens
#Two turtle doves
#And a partridge in a pear tree.

text_list = {
    1: {  
        "cardinal": "first",
        "text": "A partridge in a pear tree."
    },
    2: {
        "cardinal": "second",
        "text": "Two turtle doves and"
    },
    3: {
        "cardinal": "third",
        "text": "Three french hens"
    },
    4: {
        "cardinal": "forth",
        "text": "Four calling birds"
    },
    5: {
        "cardinal": "fifth",
        "text": "Five golden rings"
    },
    6: { 
        "cardinal": "sixth",
        "text": "Six geese a-laying"
    },
    7: {
        "cardinal": "seventh",
        "text": "Seven swans a-swimming"
    },
    8: {
        "cardinal": "eigth",
        "text": "Eight maids a-milking"
    },
    9: {
        "cardinal": "ninth",
        "text": "Nine ladies dancing"
    },
    10: {
        "cardinal": "tenth",
        "text": "Ten lords a-leaping"
    },
    11: {
        "cardinal": "eleventh",
        "text": "Eleven pipers piping"
    },
    12: {
        "cardinal": "Twelfth",
        "text": "Twelve drummers drumming"
    },
}

def print_main_text(cardinal):
    return "On the " + cardinal + " day of Christmas,\nMy true love gave to me:\n"

def iterate_and_print(text_list, num):
    text = ""
    for i in range(num, 0, -1):
        text = text + text_list[i]['text'] + "\n"
    return text

def full_verse(text_list, num):
    return print_main_text(text_list[num]['cardinal']) + iterate_and_print(text_list, num)

def iterate_full_verse(text_list):
    text = ""
    for i in range(1, len(text_list) + 1):
        text = text + full_verse(text_list, i) + "\n"
    return text