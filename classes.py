class Loc:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

class Car:

    def __init__(self, loc):
        self.loc = loc

    def get_loc(self):
        return self.loc

    def set_loc(self, loc):
        self.loc = loc

    def setX(self, x):
        loc = self.loc
        loc.setX(x)
        self.set_loc(loc)

    def setY(self, y):
        loc = self.loc
        loc.setY(y)
        self.set_loc(loc)

    def setXY(self, x, y):
        loc = self.loc
        loc.setXY(x ,y)
        self.set_loc(loc)

    def getX(self):
        loc = self.get_loc()
        return loc.getX()

    def getY(self):
        loc = self.get_loc()
        return loc.getY()

    def getXY(self):
        loc = self.get_loc()
        return loc.getX(), loc.getY()

class Ride:

    def __init__(self, start_loc, end_loc, start_time, end_time):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.start_time = start_time
        self.end_time = end_time
        self.is_done = False

    def get_start_loc(self):
        return self.start_loc

    def get_end_loc(self):
        return self.end_loc

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def is_done(self):
        return self.is_done

    def set_done(self):
        self.is_done = True


