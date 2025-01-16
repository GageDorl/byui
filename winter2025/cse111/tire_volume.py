import math
from datetime import datetime

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi*(width**2)*ratio*(width*ratio+2540*diameter))/10000000000

decision = input(f'The approximate volume is {volume:.2f} liters.\nWould you like to buy tired with these dimensions?(yes/no) ')
with open('volume.txt','a') as volume_file:
    if decision.lower() == 'yes':
        number = input('Please enter your phone number: ')
        volume_file.write(f'{datetime.now():%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {number}\n')
    else:
        volume_file.write(f'{datetime.now():%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}\n')