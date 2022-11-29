class Token:

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def __repr__(self):
        return f"({self.type}, {self.content})"