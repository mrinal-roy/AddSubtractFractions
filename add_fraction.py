from add_fraction_call_func import lcmOfTwoNos
from add_fraction_call_func import denoLCM

print("How many fractions you want to add:")
N = int(input())

fraction = []
for entry in range(1,N+1):
    print('Enter Numerator of Fraction {}'.format(entry))
    Numerator = int(input())
    print('Enter Denominator of Fraction {}'.format(entry))
    Denominator = int(input())
    t = (Numerator,Denominator)
    fraction.append(t)
print(fraction)
  
denoList = []

for each in fraction:
    denoList.append(each[1])

lcmDenominator = denoLCM(denoList)

Numerator_Sum = 0
for eachNum in range(len(fraction)):
    Numerator_Sum = (Numerator_Sum + int((lcmDenominator/fraction[eachNum][1]))*fraction[eachNum][0])
  
print('{}'.format(Numerator_Sum))
print('{}'.format('--'))
print('{}'.format(lcmDenominator))
