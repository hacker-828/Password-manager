import random
import string

def password_gen(password_op1, password_op2, password_op3):
     number = 8
     special_characters= [
     '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
     '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',
     ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?',
     '`', '~'
     ]
     capital_letters = list(string.ascii_uppercase)
     small_letters = list(string.ascii_lowercase)
     numbers = list(string.digits)
# ABC
     if password_op1 == "A" and password_op2 == "B" and password_op3 == "C":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randsmall = random.choices(small_letters)
               password_generated ="".join(randcapital) + "".join(randsmall)
               passw = passw + password_generated
          print(passw)
# ABD
     elif password_op1 == "A" and password_op2 == "B" and password_op3 == "D":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randnumber = random.choices(numbers)
               password_generated ="".join(randcapital) + "".join(randnumber)
               passw = passw + password_generated
          print(passw)
# ABE
     elif password_op1 == "A" and password_op2 == "B" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randspecial = random.choices(special_characters)
               password_generated ="".join(randcapital) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)
# ACD
     elif password_op1 == "A" and password_op2 == "C" and password_op3 == "D":
          passw = ""
          for i in range(number):
               i =+ 1
               randsmall = random.choices(small_letters)
               randnumber = random.choices(numbers)
               password_generated ="".join(randsmall) + "".join(randnumber)
               passw = passw + password_generated
          print(passw)
# ACE
     elif password_op1 == "A" and password_op2 == "C" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randsmall = random.choices(small_letters)
               randspecial = random.choices(special_characters)
               password_generated ="".join(randsmall) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)
#   AelDE        
     elif password_op1 == "A" and password_op2 == "D" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randnumber = random.choices(numbers)
               randspecial = random.choices(special_characters)
               password_generated ="".join(numbers) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)
# BCD
     elif password_op1 == "B" and password_op2 == "C" and password_op3 == "D":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randsmall = random.choices(small_letters)
               randnumber = random.choices(numbers)
               password_generated ="".join(randcapital) + "".join(randsmall) + "".join(randnumber)
               passw = passw + password_generated
          print(passw)
# BCE
     elif password_op1 == "B" and password_op2 == "C" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randsmall = random.choices(small_letters)
               randspecial = random.choices(special_characters)
               password_generated ="".join(randcapital) + "".join(randsmall) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)
# BDE
     elif password_op1 == "B" and password_op2 == "D" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randcapital = random.choices(capital_letters)
               randnumber = random.choices(numbers)
               randspecial = random.choices(special_characters)
               password_generated ="".join(randcapital) + "".join(numbers) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)
# CDE
     elif password_op1 == "C" and password_op2 == "D" and password_op3 == "E":
          passw = ""
          for i in range(number):
               i =+ 1
               randsmall = random.choices(small_letters)
               randnumber = random.choices(numbers)
               randspecial = random.choices(special_characters)
               password_generated ="".join(randsmall) + "".join(numbers) + "".join(randspecial)
               passw = passw + password_generated
          print(passw)