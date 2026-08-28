'''
Question:
Take a month number (1–12) and print the number of days in that month.
Ignore leap years.

Test Cases:

Input: 1
Output: 31

Input: 2
Output: 28

Input: 4
Output: 30

Input: 12
Output: 31
'''



n = int(input("Enter The Number: "))

# l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# if 1 <= n <= 12:
#     print(l[n - 1])
# else:
#     print("Invalid Range")




if 1 <= n <= 12:

    if n == 2:
        print(28)

    elif n == 4 or n == 6 or n == 9 or n == 11:
        print(30)

    else:
        print(31)

else:
    print("Invalid Range")