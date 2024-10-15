grade = float(input('What is your grade? '))
letterGrade=''
if(grade>=90):
    letterGrade='A'
elif(grade>=80):
    letterGrade='B'
elif(grade>=70):
    letterGrade='C'
elif(grade>=60):
    letterGrade='D'
else:
    letterGrade='F'
if(grade>=60 and grade<95):
    if(grade%10>=7):
        letterGrade+='+'
    elif(grade%10<3):
        letterGrade+='-'
if(grade>=70):
    if(letterGrade=='A'):
        print(f'Good job! You passed with an {letterGrade}!')
    else:
        print(f'Good job! You passed with a {letterGrade}!')
else:
    print(f'Sorry bud, you failed the class with a {letterGrade}, but you\'ll get them next time')