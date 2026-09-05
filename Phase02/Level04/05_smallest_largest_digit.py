'''
5. Find the smallest and largest digit in a given number.

Test Case:
Input:
Enter number: 583921

Output:
Smallest digit: 1
Largest digit: 9
'''

n=int(input("Enter : "))

small=float('inf')
long=float('-inf')

while n>0:
    d=n%10

    if d>long:
        long=d
    
    if d<small:
        small=d
    
    n//=10

print("smallest",small)
print("longest",long)