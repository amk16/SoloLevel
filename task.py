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
            "Id" : self.Id,
            "exp" : self.exp,
            "reward" : self.reward,
            "complete_reqs":  self.complete_reqs,
        }
    @classmethod
    def from_dict(cls,data):
        return cls(title=data["title"], Id = data["Id"], exp = data["exp"], reward = data["reward"], complete_reqs = data["complete_reqs"])

    def edit_title(self, title):
        self.title = title

    def edit_Id(self,Id):
        self.Id = Id
    
    def edit_exp(self,exp):
        self.exp = exp

    def edit_reward(self,reward):
        self.reward = reward
    
    def edit_complete_reqs(self, complete_reqs):
        self.complete_reqs = complete_reqs

    def get_title(self):
        return self.title

    def get_Id(self):
        return self.Id

    def get_exp(self):
        return self.exp

    def get_reward(self):
        return self.reward

    def get_complete_reqs(self):
        return self.complete_reqs


    

