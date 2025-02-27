from prettytable import PrettyTable 
users = []
def sign_up():
    user = {}  
    user["name"] = input("Enter Name: ")
    user["email"] = input("Enter Email: ")
    user["password"] = input("Enter Password: ")
    users.append(user)  
    print("Sign-up successful!\n")

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    for user in users:
        try:
            if user["email"] == email and user["password"] == password:
                print("Login successful!\n")
        except Exception as e:
            print(e)

def show_users():
    if not users:
        print("No users available.\n")
        return

    table = PrettyTable(["Name", "Email"])  
    for user in users:65
        table.add_row([user["name"], user["email"]])
    
    print("\nRegistered Users:")
    print(table)

def delete_user():
    email = input("Enter Email to delete: ")
    
    for user in users:  
        if user["email"] == email:
            users.remove(user)
            print("User deleted.\n")
            return
    print("User not found.\n")

while True:
    print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        show_users()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")