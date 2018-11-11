def lcmOfTwoNos(a,b):
    '''
    This function finds the LCM of two numbers and returns
    the value of this LCM to the calling section of the program
    '''
    num1_MultipleList = []
    num2_MultipleList = []
    commonMultipleList = []

    for i in range(1,b+1):
        num1_MultipleList.append(a*i)

    for j in range(1,a+1):
        num2_MultipleList.append(b*j)

    for num1Each in num1_MultipleList:
        for num2Each in num2_MultipleList:
            if num1Each == num2Each:
                commonMultipleList.append(num1Each)
    return commonMultipleList[0]


def denoLCM(denominatorList):
    '''
    This function finds the LCM of a list of numbers and returns
    the value of this LCM to the calling section of the program
    '''

    denominatorList.sort()
    k=0
    num2 = denominatorList[k+1]
    while (k<len(denominatorList)):
        num1 = denominatorList[k]
        lcm_temp = lcmOfTwoNos(num1,num2)
        num2 = lcm_temp
        k += 1
    return lcm_temp
