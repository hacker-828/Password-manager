import random
import string

def password_gen(password_op1, password_op2, password_op3):
     number = 8

     capital_letters = list(string.ascii_uppercase)

     small_letters = list(string.ascii_lowercase)

    #  return f"{capital_letters}\n, {small_letters}\n, {special_characters} "
     if password_op1 == "A" and password_op2 == "B" and password_op3 == "c":
        for i in range in number:
            capital = random.choices(capital_letters)
            small = random.choices(small_letters)
            password_generated = "".join(capital,small)
            return password_generated
