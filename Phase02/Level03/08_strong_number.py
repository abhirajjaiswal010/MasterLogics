'''
Question:
Write a Python program to check whether a given number is a Strong Number.
A Strong Number is a number whose sum of the factorials of its digits is equal to the number itself.

Test Case:
Input:
145

Output:
Strong Number
'''
n=int(input("Enter : "))
temp=n

sum=0

while n>0:
    d=n%10
    p=1
    for i in range(1,d+1):
        p*=i
    sum+=p
    n//=10

print(sum==temp)
