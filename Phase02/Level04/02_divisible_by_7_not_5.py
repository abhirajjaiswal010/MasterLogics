'''
2. Count how many numbers between 1 and 500 are divisible by 7
   but are not divisible by 5.

Test Case:
Input: 1 to 500

Output:
58
'''

count=0

for i in range(1,501):
    if i%7==0 and i%5!=0:
        count+=1

print(count)