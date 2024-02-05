from user_profile import UserProfile
class system():
    def __init__(self):
        self.user_profile = UserProfile()


    def execute_command(self,command, *args):
        #check if the command method exists in this controller
        if hasattr(self,command) and callable(getattr(self,command)):
            method = getattr(self,command)
            method(*args)