'''
Question:
Take two numbers and determine whether both are even, both are odd,
or one is even and the other is odd.

Test Cases:

Input: 4 8
Output: Both Even

Input: 3 7
Output: Both Odd

Input: 4 7
Output: One Even and One Odd
'''

n1, n2 = map(int, input("Enter The Numbers: ").split())

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Both Even")

elif n1 % 2 != 0 and n2 % 2 != 0:
    print("Both Odd")

else:
    print("One Even and One Odd")