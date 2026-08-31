
"""
Question 4:
Take three numbers and check whether they are all equal,
all different, or any two of them are equal.

Explanation:
- If all three numbers are equal, print "All Equal".
- If all three numbers are different, print "All Different".
- Otherwise, print "Two Equal".

Test Cases:
Input  : 5 5 5
Output : All Equal

Input  : 2 4 6
Output : All Different

Input  : 5 5 8
Output : Two Equal
"""

a,b,c=map(int,input("Enter :").split())

if a==b and b==c:
    print("all equal")
elif a==b and b!=c:
    print("Two Equals")
else:
    print("All Different")


