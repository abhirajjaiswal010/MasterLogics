
"""
Question 1:
Take a character and check if it is a letter, a digit, or neither.

Explanation:
- If the character is an alphabet letter, print "Letter".
- If the character is a digit (0-9), print "Digit".
- Otherwise, print "Neither".

Test Cases:
Input  : A
Output : Letter

Input  : 7
Output : Digit

Input  : @
Output : Neither
"""

s=input("Enter : ")

if "A"<=s<="Z" or "a"<=s<="z":
    print("Letter")
elif '0'<=s<='9':
    print("Digit")
else:
    print("Neither")