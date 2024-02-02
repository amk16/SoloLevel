class Quest:
    
    def getName(self):
        return self.name
    def getLevel(self):
        return self.level
    def getContent(self):
        return self.content
    


    def __init__(self,name,level,content):
        self.name =  name
        self.level = level
        self.content = content
        