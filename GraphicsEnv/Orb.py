class Orb:
    def __init__(self, starting_position, radius, color):
        #self.width, self.height = 50, 50
        self.color = color
        self.speed = 5
        self.x, self.y = starting_position
        self.orb_radius = radius
    
    # getters
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getSpeed(self):
        return self.speed
    
    def getRadius(self):
        return self.orb_radius
    
    def getColor(self):
        return self.color
    
    def getPosition(self):
        return (self.x,self.y)
    

    # Setters
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
        
    def changeX(self, s):
        self.x += s
    
    def changeY(self, s):
        self.y += s


        

    def __str__(self):
        pass


        
