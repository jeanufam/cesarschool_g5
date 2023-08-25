class User:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name
        return False
