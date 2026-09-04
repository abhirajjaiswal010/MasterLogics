'''
Question:
Write a Python program to find the LCM of two numbers using loops.

Test Case:
Input:
12
18

Output:
36
'''
a,b=map(int,input("Enter : ").split())
c=a
d=b

if a<b:
    a,b=b,a

#a-> big b-> small

r1=0

while a%b!=0:
    r1=a%b
    temp=b
    b=r1
    a=temp
    



lcm=(c*d)//r1
print(lcm)
