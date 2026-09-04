'''
Question:
Write a Python program to find the sum of all factors of a given number.

Test Case:
Input:
12

Output:
28
'''
n=int(input("Enter : "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum+=i

print(sum)