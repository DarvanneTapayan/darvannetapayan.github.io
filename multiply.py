# Write a nested for loop program to print multiplication table in Python

number = int(input("Enter number: "))
multipliedby = int(input("Multiplied by: "))
counter = 0

while counter <= multipliedby:
    product = counter * number
    print(f"{number} x {counter} = {product}")
    counter += 1
