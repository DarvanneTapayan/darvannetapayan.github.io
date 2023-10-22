registered_email = input("Register Email: ")
email = input("Enter Email: ")

while email != registered_email:
    print("You entered a non-existing email. Try again!")
    email = input("Enter Email: ")
else:
    print("You've successfully entered your email.")