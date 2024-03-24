import os

def add_to_blacklist(user_id):
    if is_user_banned(user_id):
        print("User already in blacklist.")
        return
    blacklist_file = "data/blacklist.txt"
    with open(blacklist_file, "a") as file:
        file.write(str(user_id) + "\n")
    print("User added to blacklist successfully.")

def is_user_banned(user_id):
    blacklist_file = "data/blacklist.txt"
    if os.path.exists(blacklist_file):
        with open(blacklist_file, "r") as file:
            banned_users = file.read().splitlines()
            return str(user_id) in banned_users
    else:
        return False

def user_exists(user_id):
  try:
      with open("data/users.txt", "r") as file:
          users = file.readlines()
          users = [int(user.strip()) for user in users]
          return user_id in users
  except FileNotFoundError:
      return False

def add_user_to_list(user_id):
  try:
      with open("data/users.txt", "a") as file:
          file.write(str(user_id) + "\n")
  except FileNotFoundError:
      with open("data/users.txt", "w") as file:
          file.write(str(user_id) + "\n")