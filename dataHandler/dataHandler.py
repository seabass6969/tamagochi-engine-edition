import json
import os
class Datahandler:
    def __init__(self):
        self.STOREPATH = os.path.join("../", "store.json")
        if os.path.isfile(self.STOREPATH):
            self.FILEOPEN = open(self.STOREPATH)
    def end(self):
        self.FILEOPEN.close()
