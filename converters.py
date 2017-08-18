import numpy as np

class Converter:
    def __init__(self):
        self.names = []
    def group_names(self, item):
        try:
            return self.names.index(item)
        except:
            self.names.append(item)
            return self.names.index(item)

            

