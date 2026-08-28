'''
Question:
Take the hour of the day (0–23) and print the appropriate greeting.

Greeting:
5–11  → Good Morning
12–16 → Good Afternoon
17–20 → Good Evening
21–23 or 0–4 → Good Night

Test Cases:

Input: 8
Output: Good Morning

Input: 14
Output: Good Afternoon

Input: 19
Output: Good Evening

Input: 23
Output: Good Night
'''

hr=int(input("Enter The Time : "))

if 5<=hr<=11:
    print("GOOD MORNING")
elif 12<=hr<=16:
    print("GOOD AFTERNOOn")
elif 17<=hr<=20:
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")