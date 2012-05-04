class Vehicle(object):
    def __init__(self,_id,_speed):
        self.id = _id
        self.speed = _speed

    def draw(self,canvas):
        pass

    def __repr__(self):
        return "vehicle(%d)"%self.id


