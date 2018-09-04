import rhinoscriptsyntax as rs

p=rs.AddPoint(0,0,0)
q=rs.AddPoint(0,0,10)
t=rs.AddPoint(0,5,10)
#l=rs.AddLine(p,q)
l=rs.AddArc3Pt(p,q,t)
c=rs.AddCircle(p,5)
m=rs.RotateObject(c,p,45,None,False)
cy=rs.ExtrudeCurve(m,l)

for i in range(1,25):
    i=i*5
    p=rs.AddPoint(0,i,i)
    q=rs.AddPoint(i,i,i*10)
    t=rs.AddPoint(i,i*5,0)
    l=rs.AddArc3Pt(p,q,t)
    c=rs.AddCircle(p,5)
    m=rs.RotateObject(c,p,45,None,False)
    cy=rs.ExtrudeCurve(c,l)
