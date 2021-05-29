class Person:
    def __init__(self):
        self.name = ""
        self.times = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_times(self):
        self.times += 1

    def get_times(self):
        return self.times