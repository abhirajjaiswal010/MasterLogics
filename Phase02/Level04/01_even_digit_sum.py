'''
1. Print all numbers between 1 and 100 whose sum of digits is even.

Test Case:
Input: 1 to 100

Output:
2 4 6 8 11 13 15 17 19 20 ... 100
'''

for i in range(1,101):
    sum=0
    num=i
    while i>0:
        d=i%10
        sum+=d
        i//=10
    
    if sum%2==0:
        print(num,end=" ")