def same_structure_as(original,other):
    answer = False
    if isinstance(original, list) and isinstance(other, list):
        if len(original) == len(other):
            answer = True
            i = 0
            while i < len(original):
                if isinstance(original[i], list) and isinstance(other[i], list):
                    answer = same_structure_as(original[i], other[i])
                    if answer is False:
                        return False
                elif not isinstance(original[i], list) and not isinstance(other[i], list):
                    answer = True
                else:
                    return False
                i += 1

    return answer


if __name__ == '__main__':
    print(same_structure_as([],1))


def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)



s = same_structure_as = lambda a, b: type(a) == type(b) == list and len(a) == len(b) and all(map(s, a, b)) if type(a) == list else 1