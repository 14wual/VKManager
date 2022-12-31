"""
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""
 
try:
    import mysql.connector
    import stdiomask
except:
    print("Before taking any action, to configure the database, you must install all the requirements!")
    exit()

usser = input("Write your MySQL user: ")
passwd = stdiomask.getpass('Write your MySQL password: ')
log = False

while log == False:
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
        )
        log = True
    except:
        print("[ ✕ ] Connected Refused\nUser or Password Incorrect\nTry again.")
        
        usser = input("Write your MySQL user: ")
        passwd = stdiomask.getpass('Write your MySQL password: ')
    finally:
        print("[ ✓ ] Connected Correctly")

mycursor = mydb.cursor()

print("Creating Database")
database = "mlp"
mycursor.execute(f"CREATE DATABASE {database}")

try:
    mlp = mysql.connector.connect(
        host="localhost",
        user=usser,
        password=passwd,
        database = database
        )
except:
    print("[ ✕ ] Manually create the database.")
    exit()
finally:
    print("[ ✓ ] Created Correctly")
    mlp.execute("SHOW TABLES")

mycursor = mlp.cursor()

mycursor.execute("CREATE TABLE vault (site VARCHAR(255), usser VARCHAR(255), password VARCHAR(255), encrkey VARCHAR(255))")

print("Inserting example")

mycursor.execute("CREATE TABLE vault (site VARCHAR(255), usser VARCHAR(255), password VARCHAR(255), encrkey VARCHAR(255))")


sql = "INSERT INTO clientes (site, usser, password, encrkey) VALUES (%s, %s, %s, %s)"
val = ("site_example", "user_example", "gAAAAABjsCzYwHX4bxETnKIVkx5-boAwViKm3K75AfTOHuyYdE1CNmrVyF1bj5n__WNwWRxrxTZAZllAG66IfUuEkrwHAsz0Uj-0ujlxIKUMvuWbofzBUrw=", "DKzHwq1CiGscZchuxw7njT1o7SvZ6H4PRWGI8i5fNIM=")
mycursor.execute(sql,val)

sql2 = "INSERT INTO clientes (site, usser, password, encrkey) VALUES (%s, %s, %s, %s)"
val2 = ("site_example2", "user_example2", "gAAAAABjsCzYwHX4bxETnKIVkx5-boAwViKm3K75AfTOHuyYdE1CNmrVyF1bj5n__WNwWRxrxTZAZllAG66IfUuEkrwHAsz0Uj-0ujlxIKUMvuWbofzBUrw=", "DKzHwq1CiGscZchuxw7njT1o7SvZ6H4PRWGI8i5fNIM=")
mycursor.execute(sql2,val2)

sql3 = "INSERT INTO clientes (site, usser, password, encrkey) VALUES (%s, %s, %s, %s)"
val3 = ("site_example3", "user_example3", "gAAAAABjsCzYwHX4bxETnKIVkx5-boAwViKm3K75AfTOHuyYdE1CNmrVyF1bj5n__WNwWRxrxTZAZllAG66IfUuEkrwHAsz0Uj-0ujlxIKUMvuWbofzBUrw=", "DKzHwq1CiGscZchuxw7njT1o7SvZ6H4PRWGI8i5fNIM=")
mycursor.execute(sql3,val3)

mydb.commit()

print("[ ✓ ]", mycursor.rowcount, "Embedded example inserted")

print("[ ✓ ] MySQL Configured Successfully")
