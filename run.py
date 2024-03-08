from app import Blog
from app.models import User, Post


def run_blog():
    print("Welcome to the blog!")
    # create an instance of the Blog class
    blog = Blog()

    # CREATE SOME INITIAL DATA
    user1 = User('brians', '123')
    user2 = User('jumpman23', '123')
    blog.users.append(user1)
    blog.users.append(user2)
    post1 = Post('Fri-yay!', 'It is Friday, hooray!', user1)
    post2 = Post('Weekend', 'I am ready for the weekend', user2)
    blog.posts.append(post1)
    blog.posts.append(post2)


    # Start 'running' our blog until user quits
    while True:
        if blog.current_user is None:
            # Print the menu option
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            # Ask the user what they would like to do
            to_do = input("Which option would you like to do? ")
            options = {
                '1' : 'sign up',
                '2' : 'log in',
                '3' : 'all posts',
                '4' : 'single post',
                '5' : 'quitting',
            }
            while to_do not in options.keys():
                to_do = input("Invalid option. Please enter 1, 2, 3, 4, or 5: ")
            
            if to_do == '5':
                break
            elif to_do == '1':
                blog.create_new_user()
            elif to_do == '2':
                blog.log_user_in()
            elif to_do == '3':
                blog.view_posts()
            elif to_do == '4':
                blog.view_post()
            else:
                print(f"Option {to_do} is coming soon!")
        else:
            # Print the menu for logged in users
            print("1. Sign Out\n2. Create A Post\n3. View All Posts\n4. View Single Post\n5. Edit A Post\n6. Delete A Post")
            to_do = input("Which option would you like to do? ")
            options = {'1', '2', '3', '4', '5', '6'}
            while to_do not in options:
                to_do = input("Invalid option. Please enter 1, 2, 3, 4, 5, or 6: ")
            if to_do == '1':
                blog.log_user_out()
            elif to_do == '2':
                blog.create_new_post()
            elif to_do == '3':
                blog.view_posts()           
            elif to_do == '4':
                blog.view_post()
            elif to_do == '5':
                blog.edit_post()
            elif to_do == '6':
                blog.delete_post()
            else:
                print(f"Option coming soon")
    print("Thanks! Bye Bye!")
    print(blog.users)
    print(blog.posts)

run_blog()