import base64

accOrLog = input("If you wanna add accounts, enter 1, if you want to login, press 2: ") # Getting input if want to add accounts or login

if accOrLog == "1":
    uname = input("Enter Username To Store: ")
    pwd = input("Enter Password To Store: ")

    pwd = pwd.encode("ascii")
    pwd = base64.b64encode(pwd)
    pwd = pwd.decode("ascii")

    with open("accounts.txt", "a") as f:
        f.write(f"{uname},{pwd}\n")
        print("Account Added")

elif accOrLog == "2":
    
    ifCorrect = 0

    uname = input("Enter Username: ")
    pwd = input("Enter Password: ")

    with open("accounts.txt", "r") as f:
        accounts = f.readlines()

    for acc in accounts:
        real_acc = acc.split(",")
        real_uname = real_acc[0]
        real_pwd = real_acc[1].replace("\n", "")
        real_pwd = real_pwd.encode("ascii")
        real_pwd = base64.b64decode(real_pwd)
        real_pwd = real_pwd.decode("ascii")

        print(real_pwd)

        if uname == real_uname and pwd == real_pwd:
            ifCorrect = True
            break

    if ifCorrect:
        print("Logged in!")
    else:
        print("Wrong Credentials.")

else:
    print("Yo, you gotta enter 1 or 2.")
