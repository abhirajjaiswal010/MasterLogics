
"""
Question 7:
Take a single digit (0-9) and print its word form
("Zero" to "Nine").

Explanation:
- If the input is 0, print "Zero".
- If the input is 1, print "One", and so on up to 9.
- If the input is not a single digit, print "Invalid".

Test Cases:
Input  : 0
Output : Zero

Input  : 5
Output : Five

Input  : 9
Output : Nine

Input  : 12
Output : Invalid
"""
a=input("Enter The Num : ")
l=["zero","one","two","three","four","five","six","seven","eight","nine"]

if len(a)==1:
    print(l[int(a)])
else:
    print("only single digit")