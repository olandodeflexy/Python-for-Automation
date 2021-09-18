def get_username():
    name = str(input("Enter name: "))
    return name.lower()

def valid_username(name):
    if str(name) == "sadic":
        return True
    return False


username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
print("Welcome to your page "  + username)
