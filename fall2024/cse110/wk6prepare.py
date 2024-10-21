loanSize = int(input('On a scale from 1-10, how large is the loan? '))
creditHistory = int(input('On a scale from 1-10, how large is the loan? '))
incomeSize = int(input('On a scale from 1-10, how high is your income? '))
downPayment = int(input('On a scale from 1-10, how large is your down payment? '))
if loanSize>=5:
    if creditHistory>=7 and incomeSize>=7:
        decision = True
    elif creditHistory>=7 or incomeSize>=7:
        if downPayment>=5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if creditHistory<4:
        decision = False
    elif incomeSize>=7 or downPayment>=7:
        decision = True
    elif incomeSize>=4 and downPayment>=4:
        decision = True
    else:
        decision = False
if decision:
    print('We are happy to inform you that you have been approved for your loan')
else:
    print('We regret to inform you that you have been denied for your loan')