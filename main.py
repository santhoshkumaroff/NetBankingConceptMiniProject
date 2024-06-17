import random
import sqlite3
conn = sqlite3.connect('mydb.db')
# print(random.randrange(1000,9999,4))
# create table
# exe = conn.execute('''
# CREATE TABLE AccountDetails (
#     userid INTEGER PRIMARY KEY AUTOINCREMENT,
#     username VARCHAR(32),
#     password VARCHAR(10),
#     branchname VARCHAR,
#     bankname VARCHAR,
#     ifsc_code VARCHAR,
#     branchcode VARCHAR
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
def netbanking(userdetails):
    print("Welcome to Net Banking 😊.....")
    sender = input("Enter sender mail id : ")
    alluserdetails = list(conn.execute(f'select username from AccountDetails'))
    all_usernames = []
    usernames = []
    for i in alluserdetails:
                all_usernames.append(i[0])
    for j in all_usernames:
                usernames.append(j)
    conn.commit()
    while True:
        if sender in usernames:
            while True:
                amount = int(input("Enter amount : "))                   
                oldamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{userdetails[1]}"'''))[0][0]
                newamount = oldamount-amount
                if newamount>=0:
                    if 10000>=amount>=0:
                        while True:
                            g_otp = random.randrange(1000,9999,4)
                            u_otp = int(input(f"--------OTP-----> {g_otp}\nEnter OTP: "))
                            if g_otp == u_otp:
                                updateamount = list(conn.execute(f'''update AccountDetails set bank_balance="{newamount}" where username = "{userdetails[1]}"'''))
                                conn.commit()
                                oldsenderamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{sender}"'''))[0][0]
                                sendernewamount = oldsenderamount+amount
                                updatesenderamount = list(conn.execute(f'''update AccountDetails set bank_balance="{sendernewamount}" where username = "{sender}"'''))
                                conn.commit()
                                print('Transaction successful ✅✅✅')
                                print(f'Your oldamount Balance : {oldamount} - new balance : {newamount}')
                                # conn.commit()
                                userdetails =list(userdetails)
                                userdetails[8]=newamount
                                checkbalance(userdetails)
                                break
                            else:

                                 print("\nEnter amount 0 to 10000\n")       
                    else:
                        print("Insufficient Balance")
                    break
        else:
            print("Sender id is not available")                   
def checkbalance(userdetails):
    print(f'Your Bank Balance is {userdetails[8]}')
    while True:
        main=0
        try:
            main = int(input("Press 7 to back menu : "))
        except:
            print("Invalid Option ❌❌❌")
        if main ==7:
            showdetails(userdetails)
            break
        else:
            print("Wrong option enter 7 to main menu : ")
            
def addamount(userdetails):
    print(userdetails)
    while True:
        while True:
                g_otp = random.randrange(1000,9999,4)
                u_otp=0
                u_otp = int(input(f"--------OTP-----> {g_otp}\nEnter OTP: "))
                if g_otp == u_otp:
                    while True:
                        check=0
                        try:
                            check = int(input('Do You Want to Add Amount Enter 1\nFor main menu enter 2\nEnter : '))
                        except:
                            print("Invalid Option ❌❌❌❌")
                        # alphabets = 
                        if int(check)!= 1 and int(check)!= 2:
                            print('Wrong Option ❌❌❌')
                            break
                        else:
                            if int(check)==1:
                                    amount=0
                                    amount = int(input("Don't Enter Alphabets ❌❌❌\nIf Enter Your Account Terminated\nEnter amount here 👇👇👇\nEnter : "))
                                    if 10000>=amount>=0:
                                        print(userdetails[1])
                                        oldamount = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{userdetails[1]}"'''))[0][0]
                                        newamount = oldamount+amount
                                        updateamount = list(conn.execute(f'''update AccountDetails set bank_balance="{newamount}" where username = "{userdetails[1]}"'''))
                                        print(f'Old Balance : {oldamount} -----> New Balance : {newamount}')
                                        print('Amount added to your account ✅✅✅')
                                        conn.commit()
                                        userdetails =list(userdetails)
                                        userdetails[8]=newamount
                                        checkbalance(userdetails)
                                        break
                                    else:
                                        print("\nEnter amount 0 to 10000\n")                                 
                            elif check ==2:
                                showdetails(userdetails)
                    break
                else:
                    print("Invalid OTP ❌❌❌❌")
def showdetails(userdetails):
    option = input("1. Show profile \n2. Check Balance\n3. Add amount\n4. Net Banking\n5. Logout \nSelect Option : ")
    if option.isdigit():
        match option:
            case '1':
                print(f"Name : {userdetails[9]}\nUser name : {userdetails[1]}\nAccount number: {userdetails[7]}\nBank Name : {userdetails[4]}\nBranch Name : {userdetails[3]}\nIFSC CODE : {userdetails[5]}\n")
                while True:
                    main = int(input("Press 7 to back menu"))
                    if main ==7:
                        showdetails(userdetails)
                        break
                    else:
                        print("Wrong option enter 7 to main menu")
            case '2':
                checkbalance(userdetails)
                while True:
                    main = int(input("Press 7 to back menu"))
                    if main ==7:
                        showdetails(userdetails)
                        break
                    else:
                        print("Wrong option enter 7 to main menu")
            case '3':
                addamount(userdetails)
            case '4':
                netbanking(userdetails)
            case '5':
                pass
            case _:
                print("Enter Valid Option ❌❌")
                showdetails(userdetails)
            
            

def loginpasscheck(username,dbpassword,userdetails):
    userpassword = input("Enter your Password : ")
    userdetails = list(conn.execute(f'select * from AccountDetails where password="{userpassword}"'))
    all_passwords = []
    passwords = []
    for i in userdetails:
            all_passwords.append(i[2])
    for j in all_passwords:
            passwords.append(j)
    conn.commit()
    login_user = list(conn.execute(f'select * from AccountDetails where username="{username}"'))
    if userpassword == dbpassword:
        print('\nLogin Successful ✅ .....\n')
        print(login_user[0])
        showdetails(login_user[0])
    else:
        print('Wrong Password ❌ \nEnter Valid User Password')
        loginpasscheck(username,dbpassword,userdetails)

def loginusernamecheck():
    while True:
        username = input("Enter your User name : ").lower()
        userdetails = list(conn.execute(f'select username from AccountDetails'))
        all_usernames = []
        usernames = []
        for i in userdetails:
                all_usernames.append(i[0])
        for j in all_usernames:
                usernames.append(j)
        conn.commit()
        if username in usernames:
            userdetails = list(conn.execute(f'select * from AccountDetails where username="{username}"'))[0]
            print("Valid User Name ✅")
            dbpassword = userdetails[2]
            loginpasscheck(username,dbpassword,userdetails)
            break
        else:
            print('Wrong User ❌ \nEnter Valid User Name')
# register user details
def register():
    while True:
        full_name = input("Enter your full name here 👇👇👇\nEnter : ")
        username = input("Enter Mail ID example : name@gmail.com \nEnter User Name : ").lower()
        if username.endswith("@gmail.com") and len(username)>10:
            dballusernames= list(conn.execute('''select username from AccountDetails'''))
            dbusername=[]
            allusername = set({})
            for i in dballusernames:
                dbusername.append(list(i)[0])
                for j in dbusername:
                    allusername.add(j)
            # Checking Username is present or not
            if username not in allusername:
                option = int(input("1. BANGALORE\n2. CHENNAI\nEnter Option: "))
                
                # Fetching IFSC Codes,Branch names,City,Bank Name
                
                match option:
                    case 1:
                        allbranch_name = list(conn.execute(f'''select BRANCH_NAME from SBI_IFSC where CITY_NAME = "BANGALORE"'''))
                        city_name = 'BANGALORE'
                        requiredbranch_name = []
                        branch_name = []
                        for i in allbranch_name:
                                requiredbranch_name.append(i[0])
                        for j in requiredbranch_name:
                                branch_name.append(j)
                        conn.commit()
                        print(branch_name)
                        while True:
                            branchname = input("Enter Branch Name : ").upper().strip()
                            if branchname in branch_name:
                                ifsc_code = list(conn.execute(f'''select ifsc_code from SBI_IFSC where BRANCH_NAME = "{branchname}"'''))[0][0]
                                bank_name = list(conn.execute(f'''select BANK_NAME from SBI_IFSC where BRANCH_NAME = "{branchname}"'''))[0][0]
                                break
                            else:
                                print('Enter Valid Branch Name ❌....')
                    case 2:
                        allbranch_name = list(conn.execute(f'''select BRANCH_NAME from SBI_IFSC where CITY_NAME = "CHENNAI"'''))
                        city_name = 'CHENNAI'
                        requiredbranch_name = []
                        branch_name = []
                        for i in allbranch_name:
                                requiredbranch_name.append(i[0])
                        for j in requiredbranch_name:
                                branch_name.append(j)
                        conn.commit()
                        print(branch_name)
                        while True:
                            branchname = input("Enter Branch Name : ").upper().strip()
                            if branchname in branch_name:
                                ifsc_code = list(conn.execute(f'''select ifsc_code from SBI_IFSC where BRANCH_NAME = "{branchname}"'''))[0][0]
                                bank_name = list(conn.execute(f'''select BANK_NAME from SBI_IFSC where BRANCH_NAME = "{branchname}"'''))[0][0]
                                # print(ifsc_code)
                                break
                            else:
                                print('Enter Valid Branch Name ❌....')                
                while True:
                    password = input("Please Enter 6 digit\nEnter Password : ").lower()
                    if len(password) == 6:
                        confrimpassword = input("Reenter Password : ").lower()
                        if password == confrimpassword:
                            account_number = random.randrange(10000000000,99999999999,11)
                            insertdata = conn.execute(f'''insert into AccountDetails (username,password,branchname,bankname,branchcode,city_name,account_number,full_name) values("{username}","{confrimpassword}","{branchname}","{bank_name}","{ifsc_code}","{city_name}","{account_number}","{full_name}")''')
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
            print('Invalid Mail')
            continue
        break
def start():
    # try:
        option = int(input("Select option \n1. Login \n2. Register\nEnter Option : "))
        match option:
            case 1:
                loginusernamecheck()
            case 2:
                register()
            case _:
                print("\nWrong Option ❌\n")
                return start()
    # except:
    #     print("Please Enter Numbers Only")
    #     start()
    
start()
conn.commit()
