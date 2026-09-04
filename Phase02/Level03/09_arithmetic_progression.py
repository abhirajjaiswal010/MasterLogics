'''
Question:
Write a Python program to print the first n terms of an Arithmetic Progression (AP) given its first term (a) and common difference (d).

Test Case:
Input:
a = 2
d = 3
n = 5

Output:
2 5 8 11 14
'''

a,d,n=map(int,input("Enter a d n : ").split())


for i in range(n):
    ans=a+(i*d)
    print(ans)