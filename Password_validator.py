"""
PYTHON CHALLENGE: THE MULTI-STAGE SECURITY CHECK
-----------------------------------------------
Your task is to write the logic for three separate security modules. 
Follow the requirements for each question carefully.
"""

# --- QUESTION 1: THE BASIC GATEKEEPER ---
# 1. Ask for a password input.
# 2. If it's shorter than 6 characters, print "Too Short".
# 3. If it's "123456" OR "password", print "Too Simple".
# 4. Otherwise, print "Validating...".

# Write logic here:
password = input("Question 1 - Set a password: ")
len_pass = len(password)
while len_pass < 6:
    print ("Password is too short")
    password = input("Question 1 - Set a password: ")
    len_pass = len(password)
    while password == str ("123456") or password == str ("password"):
          print("Password is too simple")
          password = input("Question 1 - Set a password: ")
    else:
        len_pass = len(password)
        len_pass >= 6
else:
    len_pass = len(password)
    len_pass >= 6
    print("Validating...")
    


# --- QUESTION 2: THE MULTI-FACTOR SIMULATION ---
# Ask for two inputs: a password AND a "PIN" (as an integer).
# 1. If the password is "Admin" AND the PIN is 9999, print "Superuser Access".
# 2. If the password is "Admin" but the PIN is wrong, print "Invalid PIN".
# 3. If the password is wrong, print "Access Denied".

pwd = input("Question 2 - Enter Password: ")
pin = int(input("Question 2 - Enter 4-digit PIN: "))
# Write logic here:
if pwd == str("Admin") and pin == int(9999):
    print("Superuser Access")
elif pwd == str("Admin") and pin != int(9999):
    print("Invalid PIN")
elif pwd != str("Admin") and pin == int(9999):
    print("Incorrect Password")
    print("Access Denied")
else:
    print("Access Denied")

# --- QUESTION 3: THE COMPLEXITY BOSS ---
# Rules for a "Master Password":
# 1. It must be between 10 and 20 characters long.
# 2. It must NOT contain the word "login" (in any case).
# 3. It must start with the character "!" or "@".
#
# If all 3 rules are met, print "Password Robust!".
# If any rule is failed, print "Weakness Detected".

master_pwd = input("Question 3 - Create Master Password: ")
# Write logic here:
pwd_len = len(master_pwd)

if pwd_len >= 10 and pwd_len <= 20:
     if "!" or "@" in master_pwd:
         if "login" not in master_pwd:
             print("Password Robust!")
         else:
             print("Weakness Detected")