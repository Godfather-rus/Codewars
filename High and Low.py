def high_and_low(numbers):
    numberslist = [int(с) for с in numbers.split()]
    numberslist.sort()
    return f'{numberslist[-1]} {numberslist[0]}'


if __name__ == '__main__':
    print(high_and_low("1 2 33 4 5"))
