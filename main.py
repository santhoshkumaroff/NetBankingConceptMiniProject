import random
import sqlite3
conn = sqlite3.connect('mydb.db')

# print(random.randrange(1000,9999,4))
# create table
# conn.execute('''
# CREATE TABLE AccountDetails (
#     userid INTEGER PRIMARY KEY AUTOINCREMENT,
#     username VARCHAR(32),
#     password VARCHAR(10),
#     branchname VARCHAR,
#     bankname VARCHAR,
#     ifsc_code VARCHAR,
#     branchcode VARCHAR,
#     full_name varchar
# )
# ''')
# # Alter table add column
# add = conn.execute('''Alter table AccountDetails add column full_name varchar''')
# conn.commit()
# exe = conn.execute('''
# CREATE TABLE SBI_IFSC (
#         ifsc_code varchar primary key,
#         BANK_NAME varchar,
#         BRANCH_NAME varchar,
#         CITY_NAME varchar
# )
# ''')
# insert values
# ins = conn.execute('''
# INSERT INTO AccountDetails (username, password, branchname, bankname, ifsc_code, branchcode)
# VALUES ("nadim@gmail.com", "nadim", "bangalore", "rbi", "RBIN00005", "050")
# ''')

# insert data to ifsc_code
# ins  = conn.execute('''
# INSERT INTO SBI_IFSC VALUES("SBIN0020732","STATE BANK OF INDIA","KOYAMBEDU","CHENNAI")
# ''')
# # delete column
# delete= conn.execute('''alter table AccountDetails drop column ifsc_code ''')
# truncate
# conn.execute('DELETE FROM AccountDetails')

# truncate = conn.execute('''DELETE FROM sqlite_sequence WHERE name = "AccountDetails"''')
# conn.commit()

def netbanking(userdetails,username):
    print("Welcome to Net Banking 😊.....")
    sender = input("Enter sender mail id : ")
    allusernames = list(conn.execute(f'select username from AccountDetails'))
    usernames = [i[0] for i in allusernames]
    if sender in usernames:
            while True:
                amount = int(input("Enter amount : "))                   
                oldamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{username}"'''))[0][0]
                newamount = oldamount-amount
                if newamount>=0 and amount<=oldamount:
                    if 10000>=amount>=0:
                        while True:
                            g_otp = random.randrange(1000,9999,4)
                            u_otp = int(input(f"--------OTP-----> {g_otp}\nEnter OTP: "))
                            if g_otp == u_otp:
                                #updating amount
                                conn.execute(f'''update AccountDetails set bank_balance="{newamount}" where username = "{username}"''')
                                conn.commit()
                                oldsenderamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{sender}"'''))[0][0]
                                sendernewamount = oldsenderamount+amount
                                #updating amount
                                conn.execute(f'''update AccountDetails set bank_balance="{sendernewamount}" where username = "{sender}"''')
                                conn.commit()
                                print('Transaction successful ✅✅✅')
                                print(f'Your oldamount Balance : {oldamount} - new balance : {newamount}')
                                # conn.commit()
                                userdetails =list(userdetails)
                                userdetails[8]=newamount
                                checkbalance(userdetails,username)
                                break
                            else:
                                print("Invalid Otp")
                    else:
                            print("\nEnter amount 0 to 10000\n")       
                else:
                        print("Insufficient Balance")
                break
    else:
            print("Sender id is not available\n---------------------------------------")
            netbanking(userdetails,username)
                               
def checkbalance(userdetails,username):
    print(f'Your Bank Balance is {userdetails[8]}')
    while True:
        main=0
        try:
            main = int(input("Press 7 to back menu : "))
        except:
            print("Invalid Option ❌❌❌")
        if main ==7:
            showdetails(userdetails,username)
            break
        else:
            print("Wrong option enter 7 to main menu : ")
            
def addamount(userdetails,username):
        while True:
                g_otp = random.randrange(1000,9999,4)
                u_otp = int(input(f"--------OTP-----> {g_otp}\nEnter OTP: "))
                if g_otp == u_otp:
                    while True:
                        check = int(input('Do You Want to Add Amount Enter 1\nFor main menu enter 2\nEnter : '))
                        print("Invalid Option ❌❌❌❌")
                        # alphabets = 
                        if check==1:
                                    amount = int(input("Don't Enter Alphabets ❌❌❌\nIf Enter Your Account Terminated\nEnter amount here 👇👇👇\nEnter : "))
                                    if 10000>=amount>=0:
                                        oldamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{username}"'''))[0][0]
                                        newamount = oldamount+amount
                                        #updating new amount
                                        conn.execute(f'''update AccountDetails set bank_balance="{newamount}" where username = "{username}"''')
                                        print(f'Old Balance : {oldamount} -----> New Balance : {newamount}')
                                        print('Amount added to your account ✅✅✅')
                                        conn.commit()
                                        userdetails =list(userdetails)
                                        userdetails[8]=newamount
                                        checkbalance(userdetails,username)
                                        break
                                    else:
                                        print("\nEnter amount 0 to 10000\n")                                 
                        elif check ==2:
                                showdetails(userdetails)
                                break
                        else:
                                print("Invalid Option ❌❌❌")
                    break
                else:
                    print("Invalid OTP ❌❌❌❌")
def showdetails(userdetails,username): 
    option = input("1. Show profile \n2. Check Balance\n3. Add amount\n4. Net Banking\n5. Logout \nSelect Option : ")
    if option.isdigit():
        match option:
            case '1':
                print(f"Name : {userdetails[9]}\nUser name : {userdetails[1]}\nAccount number: {userdetails[7]}\nBank Name : {userdetails[4]}\nBranch Name : {userdetails[3]}\nIFSC CODE : {userdetails[5]}\n")
                while True:
                    main = int(input("Press 7 to back menu"))
                    if main ==7:
                        showdetails(userdetails,username)
                        break
                    else:
                        print("Wrong option enter 7 to main menu")
            case '2':
                checkbalance(userdetails,username)
                while True:
                    main = int(input("Press 7 to back menu"))
                    if main ==7:
                        showdetails(userdetails,username)
                        break
                    else:
                        print("Wrong option enter 7 to main menu")
            case '3':
                addamount(userdetails,username)
            case '4':
                netbanking(userdetails,username)
            case '5':
                return 0
            case _:
                print("Enter Valid Option ❌❌")
                showdetails(userdetails,username)
    else:
        print("Enter Valid Option ❌❌❌ ")
def loginpasscheck(username,dbpassword):
    userpassword = input("Enter your Password : ")
    login_user = list(conn.execute(f'select * from AccountDetails where username="{username}"'))
    if userpassword == dbpassword:
        print('\nLogin Successful ✅ .....\n')
        showdetails(login_user[0],username)
    else:
        print('Wrong Password ❌ \nEnter Valid User Password')
        loginpasscheck(username,dbpassword)
def loginusernamecheck():
    while True:
        username = input("Enter your User name : ").lower()
        userdetails = list(conn.execute(f'select username from AccountDetails'))
        usernames = [i[0] for i in userdetails]
        if username in usernames:
            userdetails = list(conn.execute(f'select * from AccountDetails where username="{username}"'))[0]
            print("Valid User Name ✅")
            dbpassword = userdetails[2]
            loginpasscheck(username,dbpassword)
            break
        else:
            print('Wrong User ❌ \nEnter Valid User Name')
# register user details
def register():
    while True:
        full_name = input("Enter your full name here 👇👇👇\nEnter : ")
        username = input("Enter Mail ID example : name@gmail.com \nEnter User Name : ").lower()
        if username.endswith("@gmail.com"):
            dballusernames= list(conn.execute('''select username from AccountDetails'''))
            allusername=[i[0] for i in dballusernames]
            # Checking Username is present or not            
            if username not in allusername:
                option = int(input("1. BANGALORE\n2. CHENNAI\nEnter Option: ")) 
                # Fetching IFSC Codes,Branch names,City,Bank Name
                match option:
                    case 1:
                        allbranch_name = list(conn.execute(f'''select BRANCH_NAME from SBI_IFSC where CITY_NAME = "BANGALORE"'''))
                        city_name = 'BANGALORE'
                        branch_name = [i[0] for i in allbranch_name]
                        while True:
                            for i in range(1,len(branch_name)+1):
                                print(f'{i} : {branch_name[i-1]}')
                            option = int(input("Select option"))
                            if 1<=option<=len(branch_name):
                                ifsc_code = list(conn.execute(f'''select ifsc_code from SBI_IFSC where  BRANCH_NAME = "{branch_name[option-1]}"'''))[0][0]
                                # bank_name = list(conn.execute(f'''select BANK_NAME from SBI_IFSC where  BRANCH_NAME = "{branch_name[option-1]}"'''))[0][0]
                                bank_name = "STATE BANK OF INDIA"
                                break
                            else:
                                print('Enter Valid Option ❌....')
                    case 2:
                        allbranch_name = list(conn.execute(f'''select BRANCH_NAME from SBI_IFSC where CITY_NAME = "CHENNAI"'''))
                        city_name = 'CHENNAI'
                        branch_name = [i[0] for i in allbranch_name]
                        while True:
                            for i in range(1,len(branch_name)+1):
                                print(f'{i} : {branch_name[i-1]}')
                            option = int(input("Select option : "))
                            if 1<=option<=len(branch_name):
                                    ifsc_code = list(conn.execute(f'''select ifsc_code from SBI_IFSC where  BRANCH_NAME = "{branch_name[option-1]}"'''))[0][0]
                                    # bank_name = list(conn.execute(f'''select BANK_NAME from SBI_IFSC where BRANCH_NAME = "{branch_name[option-1]}"'''))[0][0]
                                    bank_name = "STATE BANK OF INDIA"    
                                    break
                            else:
                                    print(' Enter Valid Option ❌....')                
                while True:
                    password = input("Please Enter 6 digit\nEnter Password : ").lower()
                    if len(password) == 6:
                        confrimpassword = input("Reenter Password : ").lower()
                        if password == confrimpassword:
                            account_number = random.randrange(10000000000,99999999999,11)
                            conn.execute(f'''insert into AccountDetails (username,password,branchname,bankname,branchcode,city_name,account_number,full_name) values("{username}","{confrimpassword}","{branch_name[option-1]}","{bank_name}","{ifsc_code}","{city_name}","{account_number}","{full_name}")''')
                            conn.commit()
                            print("\nRegister success ✅ ..\n")
                            loginusernamecheck()
                            break
                        else:
                            print("\n------Password Miss Match------\n")
                    else:
                        print("Password length should be equal to 6")
            else:
                print("Username is already present ")
                register()
                break
        else:
            print('Invalid Mail ❌❌❌')
            register()
            # continue
        break
def start():
    try:
        option = int(input("Select option \n1. Login \n2. Register \n3. Exit \nEnter Option : "))
        match option:
            case 1:
                loginusernamecheck()
            case 2:
                register()
            case 3:
                return 0
            case _:
                print("\nWrong Option ❌\n")
                return start()
    except:
        print("Please Enter Valid Options numbers")
        start()
start()
conn.commit()
