import json
class UserProfile:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.strength = 0
        self.intelligence = 0
        self.dexterity = 0 
        self.constitution = 0
        self.charisma = 0
        self.skills = {}
        self.active_tasks = [] 
        self.finished_tasks = []
        self.money = 0

    def to_dict(self):
        return {
            "level": self.level,
            "experience":self.experience,
            "strength" : self.strength,
            "intelligence" : self.intelligence,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "charisma": self.charisma,
            "money": self.money,
            "skills": self.skills,
            "active_tasks": [task.to_dict() for task in self.active_tasks],
            "finished_tasks": [task.to_dict() for task in self.finished_tasks],


        }
    @classmethod
    def from_dict(cls,data):
        instance = cls()
        instance.level = data.get("level",1)
        instance.experience = data.get("experience",0)
        instance.strength =  data.get("strength",0)
        instance.dexterity = data.get("dexterity",0)
        instance.constitution =  data.get("constitution",0)
        instance.charisma = data.get("charisma",0)
        instance.money = data.get("money",0)
        instance.skills = data.get("skills", {})
        instance.active_tasks = [Task.from_dict(task) for task in data.get("active_tasks",[])]
        instance.finished_tasks = [Task.from_dict(task) for task in data.get("finished_tasks",[])]
        return instance



        
        
    #increase level
    def level_up(self):
        self.level+=1
    #handle events on level up
    def on_level_up(self):
        #Reset experience till next level
        #Raise attributes
        #Check/add for new milestones/skills

        
    #increase experience
    def exp_up(self,expPoints):
        self.experience+= expPoints
    #increase strength
    def str_up(self):
        self.strength+=1
    #increase intelligence
    def int_up(self):
        self.intelligence+=1
    #increase dex
    def dex_up(self):
        self.dexterity+=1
    #increase con
    def con_up(self):
        self.constitution+=1
    #increase char
    def char_up(self):
        self.charisma+=1
    #add skill
    def new_skill(self,skill,description):
        self.skills[skill]= description
    #add task
    def new_task(self, task):
        self.active_tasks.append(task)
    #finish task
    def end_task(self,task):
        self.finished_tasks.append(task)
        self.active_tasks.remove(task)
    #increase money
    def makin_bag(self,amount):
        self.money+= amount
    #decrease money
    def bummin_out(self,amount):
        self.money+=amount

