def square_digits(num):
    NewNum = ""
    for numeral in str(num):
        NewNumeral = pow(int(numeral), 2)
        NewNum = NewNum + str(NewNumeral)
    return int(NewNum)

def square_digits2(num):
    return int(''.join(str(int(d)**2) for d in str(num)))