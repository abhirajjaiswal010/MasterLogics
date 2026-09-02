'''
Docstring for Phase01.Level05.01PointAxisCheck
1. Take coordinates (x, y) and check if the point lies on the X-axis,
   Y-axis, at the origin, or in any of the four quadrants.

   Test Cases:
   Input: (0, 0)
   Output: Origin

   Input: (5, 0)
   Output: X-axis

   Input: (0, -3)
   Output: Y-axis

   Input: (4, 5)
   Output: Quadrant I

   Input: (-4, 5)
   Output: Quadrant II

   Input: (-4, -5)
   Output: Quadrant III

   Input: (4, -5)
   Output: Quadrant IV
'''

a,b=map(int,input("Enter The X And Y : ").split())

if a>0 and b>0:
    print("Quadrant I")
elif a<0 and b<0:
    print("Quadrant III")
elif a>0 and b<0:
    print("Quadrant IV")
elif a<0 and b>0:
    print("Quadrant II")
elif a==0 and (b>0 or b<0):
    print("X-Axis")
elif b==0 and (a>0 or a<0):
    print("Y-Axis")
else:
    print("origin")