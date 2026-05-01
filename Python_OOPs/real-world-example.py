class User:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.email = input("Enter your email: ")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

# Create an instance of the User class
user1 = User()
# Display the user's information
user1.display_info()            


class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(self.name, "logged in")

class Admin(User):
    def delete_user(self):
        print("User deleted")

admin = Admin("Kamlesh")
admin.login()
admin.delete_user()