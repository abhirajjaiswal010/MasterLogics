'''
Question:
Write a Python program to find the HCF (GCD) of two numbers using loops.

Test Case:
Input:
48
18

Output:
6
'''

a,b=map(int,input("Enter : ").split())

if a<b:
    a,b=b,a

#a-> big b-> small

r1=0

while a%b!=0:
    r1=a%b
    temp=b
    b=r1
    a=temp
    

print(f"r={r1},a={a},b={b}")



