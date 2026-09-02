'''
Docstring for Phase01.Level05.04ClockAngle
4. Take time (hours and minutes) and print the smaller angle between
   the hour and minute hands of a clock.

   Test Cases:
   Input: 3 0
   Output: 90 degrees

   Input: 6 0
   Output: 180 degrees

   Input: 12 0
   Output: 0 degrees

   Input: 3 30
   Output: 75 degrees

   Input: 12 30
   Output: 165 degrees
'''
hrs,min=map(int,input("Enter The Hrs and Min : ").split())


angle=abs(30*hrs-5.5*min)

if angle >180:
    angle=360-angle
    
print(angle)
