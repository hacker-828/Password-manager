from package import password_generator

print(" Hello And Welcom To The PASSWORD-MAMAGER PRO")

print("What Dod U Wanna Do Today:\n\
    1. Generate a new Password\n\
    2. See a specific Password\n\
    3. See all saved Password\n\
")

operation = input("ENTER THE OPERATION YOU WILL LIKE TO USE: ")

if len(operation) == 0:
    print("Enter a valid operation")
else:
    generate_pass = "1"
    spacific_pass = "2"
    all_pass = "3"

    operation = operation.lower()
    if operation == generate_pass :

        link = input("Enter the Link of the site: ")
        user_name = input("Enter you User-Name: ")
        print (" choose the password options you will like to use, to generate your random password")
        print("\n\
            A. Lenght of password (between 8 to 32 characters)\n\
            B. Include capital letters (A-Z)\n\
            C. Include small (a-z)\n\
            D. Include Number (0-9)\n\
            E. Include special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)\n\
        ")
        print("Choose '3' Options above\n")
        password_op1 = input("OPTION 1: ")
        password_op2 = input("OPTION 2: ")
        password_op3 = input("OPTION 3: ")

        print(password_generator.password_gen(password_op1, password_op2, password_op3))

    elif operation == spacific_pass:
       
        print("")
    elif operation == all_pass:
       
        print("")
