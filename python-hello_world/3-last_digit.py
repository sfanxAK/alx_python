#This program will assign a random signed number to the variable number each time it is executed
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    negative_last_digit = last_digit * -1
    print("Last digit of" ,number ,"is",negative_last_digit, "and is less than 6 and not 0")
elif last_digit > 5:
    print("Last digit of" ,number ,"is",last_digit, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of" ,number ,"is",last_digit, "and is less than 6 and not 0")
elif last_digit == 0:
    print("Last digit of" ,number ,"is",last_digit, "and is 0")
