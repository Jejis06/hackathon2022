import os
import subprocess
import json

class Database:
    def __int__(self, name, parent):
        self.name = name
        self.absloute_dir = os.path.join(os.getcwd(),parent)
        self.pth = os.path.join(self.absloute_dir,self.name)
        self.data = self.connect()
        pass

    def connect(self):
        if not os.path.isfile(self.pth):
            self.build()
            return {}

        with open(self.pth, "r") as file:
            data = json.load(file)
        return data

    def build(self):
        with open(self.pth,"w") as f: f.close()

    def add_row(self,data_block):
        with open(self.pth, "r+") as file:
            self.data.append(data_block)
            file.seek(0)
            json.dump(self.data, file,indent = 6)

        return True

    def retr(self, ind): # return data block from where query is
        if self.data is None:
            return None
        return self.data[ind]


