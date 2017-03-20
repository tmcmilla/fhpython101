
import rectangle
import circle
import shape

r = rectangle.Rectangle()
r.setLength(5)
r.setWidth(10)
c = circle.Circle()
c.setRadius(5)
print(r.area())
print(r)

#s = shape.Shape()
print(r.__dict__) # {'width': 10, 'length': 5}
#print(sys.platform)
