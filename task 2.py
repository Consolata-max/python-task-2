import string
import random

# user inputs
x = input('Enter your First name: \t')
y = input('Enter your Last name: \t')
z = input('Enter your Email Address: \t')

#password generator
length = 5
random.choice(string.ascii_letters)
added = ''.join (random.choice("(string.ascii_letters") for i in range(length) )

# password 
first_name_part = x[:2]
second_name_part = y[-2:]
password = first_name_part + second_name_part + added
print (password)

# Password validation
satisfied = input('Are you satisfied with password? Yes or NO: ')

if satisfied.lower = No:
password = input('input your desired password: \t'
 if len(password) >= 7:
           print("'your password is set to: \t '", password)
else:
password = input("enter a password that is 7 characters long: ")
    else :
         print("Congratulations", x, "your password is:", password)


#user data container
 First user  = {'firstname': '', 'Secondname': '', 'password': ''}
   Second user = {'firstname': '', 'Secondname': '', 'password':'' }
   print ("First user+ Second user")