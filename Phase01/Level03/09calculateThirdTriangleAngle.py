'''
Question 9:

Take two angles of a triangle and compute the third angle.

Example 1:
Input:
Angle 1 = 60
Angle 2 = 80

Output:
Third angle = 40

Example 2:
Input:
Angle 1 = 90
Angle 2 = 30

Output:
Third angle = 60

Note:
The sum of all three angles of a triangle is 180 degrees.
'''

a1,a2=map(int,input("Enter The Angle 1 and Angle 2 : ").split())

a3=180-(a1+a2)

print(f"Third Angle : {a3}")