import json
from user_profile import UserProfile # change this to import the created user in main.py

"""Change user profile to the correct instantiated one being used"""

user_profile = UserProfile() # 
def save_data(user_profile,filename="user_profile.json"):
    #Save user profile to json file
    data = user_profile.to_dict()
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)

def load_user_data(filename="user_profile.json"):
    with open(filename,"r") as file:
        data = json.load(file)
    
    return UserProfile.from_dict(data)

