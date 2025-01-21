start = int(input('Enter the first odometer reaeding (miles): '))
end = int(input('Enter the second odometer reading (miles): '))
gallons = float(input('Enter the amount of fuel used (gallons): '))

def mpg(start, end, gallons):
    mpg = (end - start) / gallons
    print(f'{mpg:.1f} miles per gallon') 
    return mpg
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    print(f'{lp100k:.2f} liters per 100 kilometers')

def main():
    goToLp100k = mpg(start, end, gallons)
    lp100k_from_mpg(goToLp100k)


