from app.models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []

    # Method to create a new user instance
    def create_new_user(self):
        # Get user info
        username = input("Please enter a username: ")
        while username in {u.username for u in self.users}:
            print(f"{username} is already taken")
            username = input("Enter a different username: ")
        
        password = input("Please enter a password: ")
        # Create an instance of the User class
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"{new_user} has been created.")
