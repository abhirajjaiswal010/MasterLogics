'''
Docstring for Phase01.Level05.10CenturyFromYear
10. Take a year and print the corresponding century.

    Test Cases:
    Input: 1900
    Output: 19th century

    Input: 1901
    Output: 20th century

    Input: 2000
    Output: 20th century

    Input: 2001
    Output: 21st century

    Input: 2026
    Output: 21st century

    Input: 2101
    Output: 22nd century
'''

n=int(input("Enter The Year "))


first=n//1000
second=(n%1000)//100

main=(first*10)+second
# print(main)

if main*100==n:
    print(f"{main} century")
elif main*100<n:
    print(f"{main+1} century")
else:
    print(f"{main} century")

