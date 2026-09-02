"""
05. MULTIPLICATION TABLE

Write a Python program to take a number n as input
and print its multiplication table from n × 1 to n × 10.
"""

n=int(input("Enter The Number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")