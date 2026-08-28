"""
Question:
Take a day number (1–7) and print the corresponding day name.

Test Cases:

Input: 1
Output: Monday

Input: 4
Output: Thursday

Input: 7
Output: Sunday
"""

n = int(input("Enter The Nnumber  : "))
l = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

if 1 <= n <= 7:
    for i in range(len(l)):
        if i == n - 1:
            print(l[i])
            break
else:
    print("Invalid Range")
