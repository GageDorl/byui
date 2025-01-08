import math

def compute_area(shape, length, width=1):
    if shape == 'square':
        return length**2
    elif shape == 'circle':
        return math.pi*radius**2
    elif shape =='rectangle':
        return length*width

choice = input('What kind of shape do you have? SQUARE, RECTANGLE, CIRCLE, or QUIT ').lower()

while choice != 'quit':
    if choice == 'square':
        side = float(input('What is the length of the side of the square? '))
        print(f'A square with a side length of {side} has an area of {compute_area('square',side)}')
    
    elif choice == 'rectangle':
        side = float(input('What is the length of the rectangle? '))
        side2 = float(input('What is the width of the rectangle? '))
        print(f'A rectangle with a length of {side} and a width of {side2} has an area of {compute_area('rectangle',side, side2)}')
    
    elif choice == 'circle':
        radius = float(input('What is the radius of the circle? '))
        print(f'A circle with a radius of {radius} has an area of {compute_area('circle',radius)}')
    
    else:
        print('That\'s not a choice bucko, try again')
    
    choice = input('What kind of shape do you have? SQUARE, RECTANGLE, CIRCLE, or QUIT ').lower()
print('Bye bye')