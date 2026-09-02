'''
Docstring for Phase01.Level05.06GeometricProgression
6. Take three numbers and check if they are in geometric progression.

   Test Cases:
   Input: 2 4 8
   Output: Geometric Progression

   Input: 3 9 27
   Output: Geometric Progression

   Input: 5 10 20
   Output: Geometric Progression

   Input: 2 4 10
   Output: Not Geometric Progression

   Input: 5 5 5
   Output: Geometric Progression
'''
a,b,c=map(int,input("Enter The Numbers : ").split())


if b*b==a*c:
    print("GP")
else:
    print("Not ")