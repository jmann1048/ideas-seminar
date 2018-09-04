import rhinoscriptsyntax as rs
import Rhino
p=rs.AddPoint(0,0,5)
q=rs.AddPoint(0,5,0)
l=rs.AddLine(p,q)
plane = Rhino.Geometry.Plane.WorldXY
rs.AddRectangle(plane,10,10)
for i in range(1,20):
    p=rs.AddPoint(0,0,i*5)
    q=rs.AddPoint(0,i*5,i)
    l=rs.AddLine(p,q)
    re=rs.AddRectangle(plane,i*2,i)
    start = rs.GetPoint("p")
    end = rs.GetPoint("q")
    translation = end-start
    rs.MoveObject(re,translation)
    d=rs.ExtrudeCurve(re,l)

