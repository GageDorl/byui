import math

length = float(input('Length of pendulum (meters): '))
print(f'Time (seconds): {2*math.pi*(math.sqrt(length/9.81)):.2f}')