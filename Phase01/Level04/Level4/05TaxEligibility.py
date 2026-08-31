
"""
Question 5:
Take income and age, and check if eligible for tax
(age > 18 and income > 5 L).

Explanation:
- If the person's age is greater than 18 AND income is
  greater than 5 lakh, print "Eligible for Tax".
- Otherwise, print "Not Eligible for Tax".

Test Cases:
Input  : Age = 25, Income = 600000
Output : Eligible for Tax

Input  : Age = 17, Income = 600000
Output : Not Eligible for Tax

Input  : Age = 25, Income = 400000
Output : Not Eligible for Tax
"""

age=int(input("Enter The Age : "))
income=int(input("Enter The Income : "))

if age>18 and income >500000:
    print("Eligible for Tax")
else:
    print("Not Eligible For tax")
