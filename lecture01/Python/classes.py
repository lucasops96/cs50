class Point():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def get_x(self):
        return self.x 


p = Point(4,6)
print(p.x)
print(p.get_x())