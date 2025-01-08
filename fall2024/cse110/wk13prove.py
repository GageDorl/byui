temperature = float(input("What is the temperature? "))
unit = input('Fahrenheit or Celsius (F/C)? ').upper()

def convertCelsius(temperature):
    return temperature*9/5+32

def getChill(temperature, windspeed):
    return 35.74 + (.6215*temperature)-(35.75*i**.16)+(.4275*temperature*windspeed**.16)

if unit == 'C':
    temperature = convertCelsius(temperature)

for i in range(5,65,5):
    print(f'At temperature {temperature:.1f}F, and wind speed {i} mph, the windchill is: {getChill(temperature,i):.2f}F')