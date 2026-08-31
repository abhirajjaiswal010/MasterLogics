
"""
Question 9:
Take electricity units consumed and calculate the bill
as per slabs (using if-else).

Explanation:
- For the first 100 units, charge Rs. 5 per unit.
- For the next 100 units (101-200), charge Rs. 7 per unit.
- For units above 200, charge Rs. 10 per unit.
- Calculate the total electricity bill based on the
  number of units consumed.

Test Cases:
Input  : 50
Output : Rs. 250

Input  : 150
Output : Rs. 850

Input  : 250-> 100*5+100*7+50*10
Output : Rs. 1700
"""

unit=int(input("Enter The Unit : "))

total=0
if unit<100:
    total=unit*5
elif 101<=unit<200:
    total=(100*5)+((unit-100)*7)
else:
    total=(100*5)+(100*7)+((unit-200)*10)

print(total)
    