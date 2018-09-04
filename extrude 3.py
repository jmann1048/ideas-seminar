import rhinoscriptsyntax as rs
c1=rs.GetObject()
p1=rs.DivideCurveEquidistant(c1,25,True)
c2=rs.GetObject()
p2=rs.DivideCurveEquidistant(c2,25,True)
print(p1[0])
m=0
n=0
#print(p2)
for a in p1:
    p=rs.GetPoint()
    rs.AddLine(a,p)
#rs.AddLine(p1,p2)