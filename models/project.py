class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def get_data(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date
        }
    
    def display_data(self):
        return f"{self.title} | {self.due_date}"
