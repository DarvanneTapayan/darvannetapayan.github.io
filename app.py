age = int(input("Enter your age: "))

if age >= 19:
    print("adult")
elif age >= 13 and age <= 18:
    print("teenager")
else:
    print("child")
