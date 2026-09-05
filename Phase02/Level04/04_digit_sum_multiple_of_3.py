'''
4. Print all numbers between 1 and 100 whose sum of digits
   is a multiple of 3.

Test Case:
Input: 1 to 100

Output:
3 6 9 12 15 18 21 24 27 30 ... 99
'''

for i in range(1,101):
    num=i
    sum=0
    while i>0:
        d=i%10
        sum+=d
        i//=10

    if sum%3==0:
        print(num,end=" ")