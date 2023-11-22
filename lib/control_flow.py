#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    user_name = username.lower()
    if user_name == "admin" and password == "12345":
        return"Access granted"
    else:
        return"Access denied"

def hows_the_weather(temperature):
    # your code here
    if temperature > 85:
        return("It's too dang hot out there!")
    elif temperature >=40 and temperature <=65:
        return("It's a little chilly out there!")
    elif temperature <40:
        return("It's brisk out there!")
    else:
        return("It's perfect out there!")
    

def fizzbuzz(num):
    # your code here
    if num%3 == 0 and num%5 == 0:
        return("FizzBuzz")
    elif num%3 == 0:
        return("Fizz")
    elif num%5 == 0:
        return("Buzz")
    else:
        return(num)
    

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
          return num1 /num2
        else:
            return"Division by zero is not allowed!"
    else:
         print("Invalid operation!")
         return None
            