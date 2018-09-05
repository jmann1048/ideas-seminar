import rhinoscriptsyntax as rs
a=rs.GetObjects()
surface = rs.AddLoftSrf(a)
#start = rs.SurfaceAreaCentroid(surface)
curve = rs.GetObject()
u=rs.ExtrudeSurface(surface, curve)
#m=rs.GetObject()
#p=rs.DivideCurveEquidistant(m,100)
def array_between():


    rs.SelectObject(u)
    m=rs.GetObject('select the curve for path')
    amount = rs.GetInteger('How many objects in array')
    if not amount: return
    p=rs.DivideCurveEquidistant(m,amount,True)
    for i in p:
        point1 = i
        for x in p:
            point2 = x
            vector = rs.VectorCreate(point2, point1)
            copyvec = rs.VectorDivide(vector, amount - 1)

    for v in range(1, amount):
        copy = rs.CopyObject(u, copyvec * v)

    rs.UnselectObject(u)

array_between()


