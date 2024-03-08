from app.models import User, Post

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    # Private method that will get a post by its ID or return None if it doesn't exist
    def __get_post_from_id(self):
        post_id = input("What is the ID of the post that you would like to view? ")
        while not post_id.isdigit():
            post_id = input("Invalid ID. Must be an integer. Please enter ID: ")
        for post in self.posts:
            # If post's ID matches the post_id argument
            if post.id == int(post_id):
                return post
        # If we finish the loop, that means we did not find a post with that ID
        return None


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

    # Method to log a user in
    def log_user_in(self):
        # Get user credentials
        username_input = input("What is your username? ")
        password_input = input("What is your password? ")
        # Loop through the users in the blog's user list
        for user in self.users:
            if user.username == username_input and user.check_password(password_input):
                self.current_user = user
                print(f"{user} has logged in.")
                # Can leave once user is found and skip else statement
                break
        # if we go through loop without breaking
        else: #For/Else --> else will run if for loop finishes and does not break
            # Then the user/password combination is wrong
            print("Username and/or password is incorrect.")
    
    # Method to log a user out
    def log_user_out(self):
        username = self.current_user.username
        self.current_user = None
        print(f"{username} has been logged out.")
    
    # Method to add a new post to the blog, authored by the logged in user
    def create_new_post(self):
        # Check to make sure that we have a logged in user
        if self.current_user is None:
            print("You must be logged in in order to make a post.") # 401 Unauth response
        else:
            # Get the title and post from the user input
            title = input("Enter new post title: ")
            body = input("Enter new post body: ")
            #Create a new Post with the inputted info and user info
            new_post = Post(title, body, self.current_user)
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")
    
    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post) 
        else:
            print("There are currently no posts in this blog.")
    
    # Method to view a single post by ID
    def view_post(self):
        # Get the post using the private method
        post = self.__get_post_from_id()
        #check if post exists
        if post:
            print(post)
        else:
            print(f"Post with an Id of {post.id} does not exist") #404 Not Found
    
    # Method to edit a post by ID
    def edit_post(self):
        post = self.__get_post_from_id()
        if post:
            # Check to see that the logged in user is the author of the post
            if post.author == self.current_user:
                # print the post so they can see what they are editing
                print(post)

                # Ask for the new title of the post or have them skip to keep the current title
                new_title = input("Enter a new title or press enter while empty to keep: ")
                if new_title.lower() != '':
                    post.title = new_title
                new_body = input("Enter the new body text or press enter while empty to keep: ")
                if new_body.lower() != '':
                    post.body = new_body
                
                print(f"{post.title} has been updated!")
            # If user is logged in but isn't the author
            elif self.current_user is not None:
                print(f"You do not have permission to edit this post.") # 403 Forbidden
            else:
                print(f"You must be logged in to perform this action.") # 401 Unauthorized

    def delete_post(self):
        post = self.__get_post_from_id()
        if post:
            if post.author == self.current_user:
                print(post)
                you_sure = input("Are you sure you want to delete this post? This action cannot be undone. Enter 'yes' or 'y' to delete: ").lower()
                if you_sure == 'yes' or you_sure == 'y':
                    self.posts.remove(post)
                    print(f"{post.title} has been removed from the blog")
                else:
                    print(f"Okay. We will not delete {post.title}")
            elif self.current_user is not None:
                print("You do not have permission to delete this post.")
            else:
                print("You need to be logged in in order to delete posts.")


    ############################################
    ############################################
    # Method to print out a singular post
    # def view_post(self):
    #     if self.posts:
    #         post_title = input("What post would you like to view? ")
    #         for post in self.posts:
    #             if post.title == post_title:
    #                 print(post)
    #                 break
    #         else:
    #             print(f"Could not find a post called {post_title}")
    #     else:
    #         print("There are currently no posts in this blog.")
    
    # def edit_post(self):
    #     post = self.__get_post_from_id()
    #     if post and post.author == self.current_user:
    #         print(post)
    #         edited_body = input("Write the new body of the post here: ")
    #         if edited_body:
    #             post.body = edited_body
    #         print("Here is the new post\n", post)
    #     else:
    #         print(f"Post with an Id of {post.id} does not exist or not right author.")
    
    # def delete_post(self):
    #     post_title = input("What post would you like to delete? ")
    #     for post in self.posts:
    #         if post.title == post_title and post.author == self.current_user:
    #             print(f"Removing {post.title}.")
    #             self.posts.remove(post)
    #             break
    #         elif post.title == post_title:
    #             print(f"You cannot delete {post.title} as you are not the author!")
    #             break
    #     else:
    #         print(f"Could not find a post called {post_title}")
    


        