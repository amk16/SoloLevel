from user_profile import UserProfile
from task import Task
class system():
    def __init__(self):
        self.user_profile = UserProfile()


    def execute_command(self,command, *args):
        #check if the command method exists in this controller
        if hasattr(self,command) and callable(getattr(self,command)):
            method = getattr(self,command)
            method(*args)

    def add_task(self,title,Id,exp,reward,complete_reqs):
        
        task = Task(title=title,Id=Id,exp=exp,reward=reward,complete_reqs=complete_reqs)
        self.user_profile.get_active_tasks().append(task)
        print(f"Task {Id}: {title} has been created")

    def complete_task(self,Id):
        for task in self.user_profile.get_active_tasks():
            if task.Id == Id:
                self.user_profile.finished_tasks.append(task)
                self.user_profile.active_tasks.remove(task)
                print(f"Task {task.getId()}: {task.getTitle()} has been completed")
                return
            else:
                print(f"Task {Id} does not exist")

    def show_tasks(self):
        print("Active tasks:")
        for task in self.user_profile.get_active_tasks():
            print(f"- {task.getId()}: {task.getTitle()}")
        
        print("Finished tasks:")
        for task in self.user_profile.get_active_tasks():
            print(f"- {task.getId()}: {task.getTitle()}")

    