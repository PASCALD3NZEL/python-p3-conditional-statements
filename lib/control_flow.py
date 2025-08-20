#!/usr/bin/env python3

def admin_login(username, password):
    """
    Validates admin credentials.
    Returns "Access granted" if username is "admin" (case-insensitive) and password is "12345".
    Returns "Access denied" for any other combination.
    """
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    """
    Returns different messages based on temperature.
    - "It's brisk out there!" for temperature around 33
    - "It's a little chilly out there!" for temperature around 55
    - "It's perfect out there!" for temperature around 75
    - "It's too dang hot out there!" for temperature around 99
    """
    if temperature <= 33:
        return "It's brisk out there!"
    elif temperature <= 60:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    """
    Classic FizzBuzz implementation:
    - Returns "FizzBuzz" if num is divisible by both 3 and 5
    - Returns "Fizz" if num is divisible by 3
    - Returns "Buzz" if num is divisible by 5
    - Returns num itself otherwise
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    """
    Performs basic arithmetic operations:
    - "+" for addition
    - "-" for subtraction
    - "*" for multiplication
    - "/" for division
    Returns None and prints "Invalid operation!" for invalid operations
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None