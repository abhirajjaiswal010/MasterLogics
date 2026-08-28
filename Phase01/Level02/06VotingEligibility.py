'''
Question:
Take a person's age and check whether they are eligible to vote.

Eligibility:
Age 18 or above → Eligible to Vote
Below 18 → Not Eligible to Vote

Test Cases:

Input: 20
Output: Eligible to Vote

Input: 18
Output: Eligible to Vote

Input: 16
Output: Not Eligible to Vote
'''

age=int(input("Enter The Age : "))

if age<18:
    print("Not Eligible To Vote ")
else:
    print("Eligible To Vote")