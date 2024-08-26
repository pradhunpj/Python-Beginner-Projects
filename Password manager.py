from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

print("Password Manager Application\n")

master_pwd = input("Enter the master password: ")

def view():
    with open("password.txt",'r') as file:
        
        for line in file:
            username, password = line.rstrip().split(":")
            print(f"Username: {username}, Password: {f.decrypt(b"password").decode()}")

def add():
    print("\nAdding your passwords")
    username = input("Enter username: ")
    pwd = input("Enter password: ")

    with open('password.txt', 'a') as file:
        encrypted_password = f.encrypt(pwd.encode()).decode()
        file.write(f"{username}:{encrypted_password}\n")
        print("Password added successfully\n")




while True:

    user_input = input("Do you want to add or view your passwords (a,v) or press Q to quit: " ).lower()
    if user_input == "q":
        exit()
    elif user_input == "a":
        add()
    elif user_input == "v":
        view()
    else:
        print("Invalid option")
        continue
