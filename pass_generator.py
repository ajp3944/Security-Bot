import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(length):

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## returning the password and converting the list to string
	return "".join(password)



## invoking the function (to be removed and replaced with the bot command input)
print(generate_random_password(14))