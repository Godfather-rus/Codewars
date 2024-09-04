from math import ceil


def snail(snail_map):
    answer = []
    count = len(snail_map)
    for i in range(ceil(len(snail_map) / 2)):
        for j in range(i, len(snail_map[i])-i, 1):
            answer.append(snail_map[i][j])

        for j in range(i + 1, count, 1):
            answer.append(snail_map[j][len(snail_map[(i*-1)])-1-i])

        for j in range(len(snail_map[i]) - 2 - i, i - 1, -1):
            answer.append(snail_map[count - 1][j])

        for j in range(count - 2, i, -1):
            answer.append(snail_map[j][i])

        count -= 1

    return answer





import numpy as np

def snail2(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


def snail3(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


if __name__ == '__main__':
    print(snail3([[1, 2, 3],
                 [4, 5],
                 [4, 5, 6],
                 [7, 8, 9]]))