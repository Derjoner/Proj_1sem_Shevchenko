class Point:
    
    "Класс для представления координат точек на плоскости"
    
    color = 'red'
    circle = 2

# print(Point.color)
# print(Point.__dict__)

pointOne = Point()
pointTwo = Point()

# print(pointOne.color)
# print(pointTwo.__dict__)

Point.circle = 3

# print(Point.circle)
# print(pointOne.circle)

pointOne.color = "green"

# print(Point.color)
# print(pointOne.color)
# print(pointTwo.color)

Point.hiddens = False
Point.inher = True

# print(Point.__dict__)
# print(pointOne.hiddens)
# print(pointTwo.inher)

# del Point.hiddens

# print(Point.__dict__)

# print(getattr(pointTwo, 'hiddens', False))
# print(getattr(pointTwo, 'inher', False))

# print(hasattr(Point, 'circle'))

if (hasattr(Point, 'inher')):
    del Point.inher
    # print(getattr(Point, 'inher', False))
    
# print(pointOne.__dict__)
# print(pointTwo.__dict__)

pointOne.like = True

# print(pointOne.__dict__)

pointOne.circle = 5

# print(pointOne.circle)

del pointOne.circle

# print(pointOne.circle)

# print(Point.hiddens == False)

Point.inher = True

