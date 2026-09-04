'''
Question:
Write a Python program to print the first n terms of a Geometric Progression (GP) given its first term (a) and common ratio (r).

Test Case:
Input:
a = 2
r = 3
n = 5

Output:
2 6 18 54 162
'''

a,r,n=map(int,input("Enter a d n : ").split())


for i in range(n):
    ans=a*(r**i)
    print(ans)