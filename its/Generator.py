import random as r

class Generator(object):
    def __init__(self, _entryIds, _adjcencyMatrix):
        self.entrys = _entryIds
        self.m = _adjcencyMatrix

    def genVehicle(self):
        start,end = r.choice(self.entrys),r.choice(self.entrys)
        while start == end:
            end = r.choice(self.entrys)
