"""Create the hack file"""


class Writer:
    def __init__(self, path):
        """Creates the hack file"""
        self.path = path
        self.file = open(self.path, 'w', newline='\n')

    def write_line(self, line):
        self.file.write(line + "\n")

    def __del__(self):
        self.file.close()
