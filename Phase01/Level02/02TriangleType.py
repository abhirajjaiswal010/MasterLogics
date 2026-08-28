'''
Question:
Take three sides of a triangle and determine whether the triangle is Equilateral,
Isosceles, or Scalene.

Definition:
Equilateral → All three sides are equal.
Isosceles → Any two sides are equal.
Scalene → All three sides are different.

Test Cases:

Input: 5 5 5
Output: Equilateral

Input: 5 5 3
Output: Isosceles

Input: 3 4 5
Output: Scalene
'''

a,b,c = map(int,input("Enter The Three Sides : ").split())


if a==b and b==c and c==a:
    print("Equilateral Triangle")
elif a==b or a==c or b==c:
    print("Isosceles Triangle")
else:
    print("Scalene")

