'''
Docstring for Phase01.Level05.02PythagoreanTriplet
2. Take three numbers and check if they can form a Pythagorean triplet.

   Test Cases:
   Input: 3 4 5
   Output: Pythagorean Triplet

   Input: 5 12 13
   Output: Pythagorean Triplet

   Input: 2 3 4
   Output: Not a Pythagorean Triplet
'''

a,b,c=map(int,input("Enter The n1 n2 and n3 : ").split())

if a>b and a>c: #a greater
    sum1=a**2
    sum2=b**2 + c**2
elif b>c : # b greater
    sum1=b**2
    sum2=a**2 + c**2
else:
    sum1=c**2
    sum2=b**2 + a**2

if sum1==sum2:
    print("pythagorean triplet")
else:
    print("not ")