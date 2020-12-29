import json

accOrLog = input("If you wanna add accounts, enter 1, if you want to login, press 2: ") # Getting input if want to add accounts or login

if accOrLog == "1":
	uname = input("Enter Username to Add: ")
	pwd = input("Enter Password to Add: ")

	with open("accounts.json", "r") as f:
		accounts = json.load(f)

	accounts[uname] = pwd

	accounts = json.dumps(accounts)

	with open("accounts.json", "w") as f:
	 	f.write(accounts)

elif accOrLog == "2":
	pass

else:
	print("You must enter 1 or 2")