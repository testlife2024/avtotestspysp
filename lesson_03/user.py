class User:
    def __init__(self,first_name,last_name):
        self.name = first_name
        self.last_name = last_name
    def name_print(self):
        print(self.name)
    def last_name_print(self):
        print(self.last_name)
    def both_print(self):
        print(self.name, self.last_name)
