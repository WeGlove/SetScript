class Token:

    def __init__(self, type, content, file,line_number, column_number):
        self.type = type
        self.content = content
        self.file = file
        self.line_number = line_number
        self.column_number = column_number

    def __repr__(self):
        return f"({self.type}, {self.content}, {self.file}:{self.line_number}:{self.column_number})"