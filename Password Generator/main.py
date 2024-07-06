from random import *

add_ons = ['@','123','!','@123','ADH','BANANA']

def new_password(words):
	global add_ons
	if " " in words:
		words.replace(" ", "")
	if "'" in words:
		words.replace("'", "")
	if '"' in words:
		words.replace('"','')
	keywords = []
	words = words.split(',')
	
	for i in words:
		keywords.append(i)

	
	for a in words:
		add_ons.append(words)
	ta = choice(add_ons)
	password = str(choice(keywords)+str(randint(10,1000))+str(ta))
	if " " in password:
		password.replace(" ", "")
	if "'" in password:
		password.replace("'", "")
	str(password)
	return password

while True:
	words = input("Enter a few words (add ',' after each word): ")
	print(new_password(words))
	

	
