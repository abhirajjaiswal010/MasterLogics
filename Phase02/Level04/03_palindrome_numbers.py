'''
3. Print all palindrome numbers between 1 and 500.

Test Case:
Input: 1 to 500

Output:
1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99
101 111 121 131 141 151 161 171 181 191
202 212 222 ... 494
'''

for i in range(1,501):
    rev=0
    num=i
    while i>0:
        d=i%10
        rev=rev*10+d
        i//=10
    if rev==num:
        print(num,end=" ")

    