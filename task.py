class Task():
    
    def __init__(self,title,Id,exp,reward,complete_reqs):
        self.title = title
        self.Id = Id
        self.exp = exp
        self.reward = reward
        self.complete_reqs = complete_reqs

    def to_dict(self):
        return {
            "title" : self.title,
            "Id" : self.title,
            "exp" : self.exp,
            "reward" : self.reward,
            "complete_reqs":  self.complete_reqs,
        }
    
    def from_dict(cls,data):
        return cls(title=data["title"], Id = data["Id"], exp = data["exp"], reward = data["reward"], complete_reqs = data["complete_reqs"])

    def edit_title(self, title):
        self.title = title
    
    def edit_exp(self,exp):
        self.exp = exp

    def edit_reward(self,reward):
        self.reward = reward


    

