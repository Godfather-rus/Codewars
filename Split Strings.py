def solution(s):
    answer = [s[i:i+2] for i in range(len(s)) if i % 2 == 0]
    if answer and len(answer[-1]) == 1:
        answer[-1] = answer[-1][0] + "_"
    return answer



def solution2(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

import re

def solution3(s):
    return re.findall(".{2}", s + "_")

if __name__ == '__main__':
    print(solution("asdasfg"))