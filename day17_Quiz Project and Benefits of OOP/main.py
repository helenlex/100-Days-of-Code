""" learning about defining classes, constructors, attributes and methods """
# defining the user class
class User:
    """ this class is to be called when a user is created. """
    # constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # method
    def follow(self, user):
        """ this method notes what happens when a user follows another user """
        user.followers += 1
        self.following += 1

# setting attributes
user1 = User("001", "angela")
user2 = User("002", "helen")

# calling the method, user 1 is following user 2
user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
