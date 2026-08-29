'''
Question 6:

Take coordinates (x, y) and determine which quadrant the point lies in.

Example 1:
Input: (3, 4)
Output: First Quadrant

Example 2:
Input: (-3, 4)
Output: Second Quadrant

Example 3:
Input: (-3, -4)
Output: Third Quadrant

Example 4:
Input: (3, -4)
Output: Fourth Quadrant

Note:
If x = 0 or y = 0, the point lies on an axis.
'''


x, y = map(int, input("Enter X and Y: ").split())

if x > 0 and y > 0:
    print("First Quadrant")

elif x < 0 and y > 0:
    print("Second Quadrant")

elif x < 0 and y < 0:
    print("Third Quadrant")

elif x > 0 and y < 0:
    print("Fourth Quadrant")

elif x == 0 and y == 0:
    print("Origin")

elif x == 0:
    print("Y-axis")

else:
    print("X-axis")