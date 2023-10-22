


def register():
    registered_email = input("Register Email: ")
    email = input("Enter Email: ")

    while email != registered_email:
        print("You entered a non-existing email. Try again!")
        email = input("Enter Email: ")
    else:
        print("You've successfully entered your email.")
        
selection = input("Select your choice: (1/2/3): ")

if selection == 1:
    register()
elif selection == 2:
    login()
elif selection == 3:
    ("exit")