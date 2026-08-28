'''
Question:
Take marks (0–100) and print the corresponding grade.

Grade:
90–100 → A
80–89  → B
70–79  → C
60–69  → D
Below 60 → F

Test Cases:

Input: 95
Output: A

Input: 82
Output: B

Input: 67
Output: D

Input: 45
Output: F
'''


g=int(input("Enter The Grade : "))

if 90<=g<=100:
    print("A")
elif 80<=g<=89:
    print("B")
elif 70<=g<=79:
    print("C")
elif 60<=g<=69:
    print("D")
else:
    print("F")