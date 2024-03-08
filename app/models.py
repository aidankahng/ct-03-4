
class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.__password = password

    def __str__(self) -> str:
        return self.username
    
    def __repr__(self) -> str:
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return self.__password == password_guess


class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        self.id = Post.id_counter
        Post.id_counter += 1
        self.title = title
        self.body = body
        self.author = author #Instance of a user

    def __str__(self) -> str:
        return f"""
    {self.id} - {self.title}
    By: {self.author}
    {self.body}
    """
    def __repr__(self) -> str:
        return f"<Post {self.id}|{self.title}>"