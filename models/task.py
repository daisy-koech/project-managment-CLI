class Task:
    def __init__(self, project_title, status, assigned_to):
        self.project_title = project_title
        self.status = status
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "Completed"
    
    def get_data(self):
        return {
            "project_title": self.project_title,
            "status": self.status,
            "assigned_to": self.assigned_to
            }
    def display_data(self):
        return f"{self.project_title} | {self.status} | {self.assigned_to}"

# task = Task("Website design", "Pending", "Daisy")
# print(task.display_data())
