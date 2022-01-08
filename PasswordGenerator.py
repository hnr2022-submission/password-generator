import string
import random


PASSWORD_LENGTH = 16

is_default = input("Would you like to use default password settings? (the default is a password of 16 characters, containing special characters, digits and letters of mixed cases ")

if(is_default.lower() != "yes"):

   PASSWORD_LENGTH = int(input("please enter the number of characters you would like your password to be? "))
   
   case = input("would you like your password to be in lowercase, uppercase or mixed case? ").lower()
   
   if case == "uppercase":
      character_list = string.ascii_uppercase
      
   elif case == "lowercase":
      character_list = string.ascii_lowercase
      
   else:
      character_list = string.ascii_letters
      
   digits = input("Would you like to have digits in your password? ").lower()
   
   if digits == "yes":
      character_list += string.digits
      
   special_characters = input("Would you like to have special characters in your password? ").lower()
   
   if special_characters == "yes":
      character_list += "!@#$%^&*()"
      
   characters = list(character_list)
   


else:
   characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():

	random.shuffle(characters)
	
	password = []
	for i in range(PASSWORD_LENGTH):
		password.append(random.choice(characters))

	random.shuffle(password)

	print("".join(password))



generate_random_password()
      
      
   
