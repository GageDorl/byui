class DataSet:
    def __init__(self, entity, code, year, life):
        self.entity = entity
        self.code = code
        self.year = year
        self.life = life

dataSets = []

with open('life-expectancy.csv') as expectancy:
    for line in expectancy:
        args = line.split(',')
        for i,arg in enumerate(args):
            args[i] = arg.strip()
        dataSets.append(DataSet(args[0],args[1],args[2],args[3]))

dataSets = dataSets[1:]
lowestLife = 100000000
lowestIndex=-1
highestIndex=-1
highestLife=0

for i, data in enumerate(dataSets):
    if float(data.life)<lowestLife:
        lowestLife=float(data.life)
        lowestIndex = i
    if float(data.life)>highestLife:
        highestLife = float(data.life)
        highestIndex = i
interest_year = int(input('Enter the year of interest: '))
print(f'\nThe overall max life expectancy is: {dataSets[highestIndex].life} from {dataSets[highestIndex].entity} in {dataSets[highestIndex].year}')
print(f'The overall min life expectancy is: {dataSets[lowestIndex].life} from {dataSets[lowestIndex].entity} in {dataSets[lowestIndex].year}')



lowestLife = 100000000
lowestIndex=-1
highestIndex=-1
highestLife=0
count=0
sum=0

for i, data in enumerate(dataSets):
    if int(data.year) == interest_year:
        sum+=float(data.life)
        count+=1
        if float(data.life)<lowestLife:
            lowestLife=float(data.life)
            lowestIndex = i
        if float(data.life)>highestLife:
            highestLife = float(data.life)
            highestIndex = i

print(f'\nFor the year {interest_year}:')
print(f'The average life expectancy across all countries was {sum/count:2f}')
print(f'The max life expectancy was in {dataSets[highestIndex].entity} with {dataSets[highestIndex].life}')
print(f'The min life expectancy was in {dataSets[lowestIndex].entity} with {dataSets[lowestIndex].life}')