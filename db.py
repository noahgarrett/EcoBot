import mysql.connector

balance = 1000
server = 273194843117977612
user = 272900275688177664
amt = 100
db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Bank"
    )
mycursor = db.cursor()

def create_server_table():
    mycursor.execute("CREATE TABLE serverBank (serverID varchar(20), userID varchar(20) PRIMARY KEY, balance int UNSIGNED)")

def delete_server_table():
    mycursor.execute("DROP TABLE serverBank")

def see_server_table():
    mycursor.execute("DESCRIBE serverBank")
    for x in mycursor:
        print(x)

async def open_account(server, user):
    server_ = str(server)
    user_ = str(user)
    mycursor.execute("INSERT INTO serverBank (serverID, userID, balance) VALUES (%s, %s, %s)", (server_, user_, balance))
    db.commit()

async def check_balance(server, user):
    try:
        server_ = str(server)
        user_ = str(user)
        result = mycursor.execute(f"SELECT balance from serverBank where userID = {user_}")
        balance = mycursor.fetchone()
        return balance[0]
    except Exception as e:
        print(e)

async def increase_balance(server, user, amt):
    try:
        server_ = str(server)
        user_ = str(user)
        balance = await check_balance(server, user)
        new_balance = int(balance) + int(amt)
        update = mycursor.execute(f"UPDATE serverBank set balance = {new_balance} where userID = {user_}")
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

async def decrease_balance(server, user, amt):
    try:
        server_ = str(server)
        user_ = str(user)
        balance = await check_balance(server, user)
        new_balance = int(balance) - int(amt)
        update = mycursor.execute(f"UPDATE serverBank set balance = {new_balance} where userID = {user_}")
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False




# create_server_table()
# see_server_table()
# delete_server_table()
# open_account(server, user)
# check_balance(server, user)

# mycursor.execute("CREATE DATABASE Bank")
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Noah", 19))
# mycursor.execute("DROP DATABASE testdatabase")