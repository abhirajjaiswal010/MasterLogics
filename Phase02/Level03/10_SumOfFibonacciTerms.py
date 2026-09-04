'''
10. Sum of First N Fibonacci Terms

Question:
Given an integer n, calculate and print the sum of the first n
terms of the Fibonacci series, starting from 0.

Test Cases:
Input: 5
Output: 7

Explanation:
Fibonacci terms = 0 1 1 2 3
Sum = 0 + 1 + 1 + 2 + 3 = 7

Input: 7
Output: 20

Input: 10
Output: 88

Input: 1
Output: 0
'''
n=int(input("Enter : "))

first=0
second=1
Msum=1

for i in range(n-2):
    sum=first+second
    Msum+=sum
    # print(sum,end=" ")
    first=second
    second=sum

print(Msum)

l=[1,2,3]
print(max(l))