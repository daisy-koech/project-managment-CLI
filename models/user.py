class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name must contain at least 2 characters")
        self._name = value

    def get_data(self):
        return{"name": self.name,
               "email": self.email}
    
    def display_data(self):
        return f"{self.name} ({self.email})"
