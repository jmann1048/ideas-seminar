import rhinoscriptsyntax as rs

allObjs = rs.AllObjects()
rs.DeleteObjects(allObjs)



class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
        
    def left(self,angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])
        print(self.direction)
        
    def right(self,angle):
        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])
        print(self.direction)
    
    def goto(self, x, y):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,0],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
    def Polygon(self,radius,sides,num,dist):
        self.num = num
        self.dist = dist
        self.radius = radius
        self.sides = sides
        theta = 360/self.sides
        pt01 = rs.AddPoint(self.radius,0,0);
        pts = []
        pts.append(pt01)
        self.origin = [0,0,0]
        degrees = theta
        for m in range(0,self.num):
            pt01 = rs.AddPoint(self.radius,0+(self.dist*m),0)
            pts.append(pt01)
            for x in range(1,self.sides):
                tempPt = pts[-1]
                newPt = rs.RotateObject(tempPt,self.origin,degrees,None,True)
                pts.append(newPt)
            pts.append(pt01)
            self.polygon = rs.AddPolyline(pts)
jash = Turtle()
jash.Polygon(5,8,10,20)