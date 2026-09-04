'''
09. Print Fibonacci Series up to N Terms

Question:
Given an integer n, print the first n terms of the Fibonacci series.

The Fibonacci series starts with 0 and 1.
Each subsequent term is the sum of the previous two terms.

Test Cases:
Input: 5
Output: 0 1 1 2 3

Input: 7
Output: 0 1 1 2 3 5 8

Input: 10
Output: 0 1 1 2 3 5 8 13 21 34

Input: 1
Output: 0
'''

n=int(input("Enter : "))

first=0
second=1
print(first,end=" ")
print(second,end=" ")
for i in range(n-2):
    sum=first+second
    print(sum,end=" ")
    first=second
    second=sum