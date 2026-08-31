
"""
Question 2:
Take a number and print "Fizz" if it is divisible by 3,
"Buzz" if it is divisible by 5, and "FizzBuzz" if it is
divisible by both.

Explanation:
- If the number is divisible by both 3 and 5, print "FizzBuzz".
- If the number is divisible only by 3, print "Fizz".
- If the number is divisible only by 5, print "Buzz".
- Otherwise, print the number.

Test Cases:
Input  : 9
Output : Fizz

Input  : 10
Output : Buzz

Input  : 15
Output : FizzBuzz

Input  : 7
Output : 7
"""

num=int(input("Enter : "))


if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0 :
    print("Fizz")
elif num%5==0:
    print("Buzz")


else:
    print(num)