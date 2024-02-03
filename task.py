class Task():
    
    def __init__(self,title,Id,exp,reward):
        self.title = ""
        self.Id = -1
        self.exp = 0
        self.reward = None
        self.complete_reqs = {}

    def edit_title(self, title):
        self.title = title
    
    def edit_exp(self,exp):
        self.exp = exp

    def edit_reward(self,reward):
        self.reward = reward


    

