def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    print(solution(-10))

def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)