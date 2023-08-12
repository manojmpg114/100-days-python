class User: #self is a reference to the object being created
    def __init__(self, user_id, username) -> None: #again the -> format is meant to guide the type testing so we return nothing in this case
        print("New user being created...")
        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
    

user_1 = User('001', 'Manoj')
user_2 = User('002', 'Keith')
# print(user_1.id)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
