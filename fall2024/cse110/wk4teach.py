import math
m = float(input('Welcome to the velocity calculator. Please enter the following:\n\nMass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
c = 1/2*(p*A*C)
ve = math.sqrt(m*9.8/c) * (1 - math.exp((-math.sqrt(m*9.8*c)/m)*t))
vj = math.sqrt(m*24/c) * (1 - math.exp((-math.sqrt(m*24*c)/m)*t))
V = ''
choice = ''
alt = ''
Valt = ''
def gravityChoice():
    if g == 9.8:
        V = ve
        choice = 'Earth'
        alt = 'Jupiter'
        Valt = vj
    elif g == 24:
        V = vj
        choice = 'Jupiter'
        alt = 'Earth'
        Valt = ve
    else:
        g = float(input('Please choose either 9.8 or 24 for gravity: '))
        gravityChoice()

print(f'\nThe inner value of c is: {c:.3f}\nThe velocity after {t:.1f} seconds is: {V:.3f} m/s on {choice}, if you had chosen {alt} it would be {Valt:.3f}')
bm = 6
bA = 0.054
bC = .5
bc = 1/2*(p*bA*bC)
bV = math.sqrt(bm*g/bc) * (1 - math.exp((-math.sqrt(bm*9.8*bc)/bm)*t))
print(f'The velocity of a bowling ball at {t:.1f} seconds is {bV} m/s on {choice}')


