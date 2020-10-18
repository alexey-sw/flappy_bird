# will help us manage our coordinates for bird
import load
arr= load.funct()
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,addx,addy):
        self.x = self.x+addx
        self.y = self.y+addy
class Bird:
    def __init__(self,images,coord):

