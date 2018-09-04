import rhinoscriptsyntax as rs
import random

points = []
for i in range(100):
    x=random.random()*10
    y=random.random()*10
    z=random.random()*10
    p=rs.AddPoint(x,y,z)
    points.append(p)
rs.AddCurve(points)