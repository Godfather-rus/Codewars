from random import choice, randint, sample, shuffle, choices
import re
from collections import Counter
from top3 import top_3_words
#import codewars_test as test


def check(s, this=None):  # this: only for debugging purpose
    returned_result = top_3_words(s) if this is None else this
    fs = Counter(w for w in re.findall(r"[a-zA-Z']+", s.lower()) if w != "'" * len(w))
    exp, expected_frequencies = map(list, zip(*fs.most_common(3))) if fs else ([], [])

    msg = ''
    wrong_words = [w for w in returned_result if not fs[w]]
    actual_freq = [fs[w] for w in returned_result]

    if wrong_words:
        msg = 'Incorrect match: words not present in the string. Your output: {}. One possible valid answer: {}'.format(
            returned_result, exp)
    elif len(set(returned_result)) != len(returned_result):
        msg = 'The result should not contain copies of the same word. Your output: {}. One possible output: {}'.format(
            returned_result, exp)
    elif actual_freq != expected_frequencies:
        msg = "Incorrect frequencies: {} should be {}. Your output: {}. One possible output: {}".format(actual_freq,
                                                                                                        expected_frequencies,
                                                                                                        returned_result,
                                                                                                        exp)
    print(msg)
    #test.expect(not msg, msg)


#@test.describe("Fixed tests")
def fixed_tests():
    TESTS = (
        "a a a  b  c c  d d d d  e e e e e",
        "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e",
        "  //wont won't won't ",
        "  , e   .. ",
        "  ...  ",
        "  '  ",
        "  '''  ",
        """In a village of La Mancha, the name of which I have no desire to cao
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""",
        "a a a  b  c c X",
        "a a c b b",
    )
    for s in TESTS: check(s)


#@test.describe("Random tests")
def random_tests():
    def gen_word():
        return "".join(choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'") for _ in range(randint(3, 10)))

    def gen_string():
        words = []
        nums = choices(range(1, 31), k=20)
        for _ in range(randint(0, 20)):
            words += [gen_word()] * nums.pop()
        shuffle(words)
        s = ""
        while words:
            s += words.pop() + "".join(choice("-,.?!_:;/ ") for _ in range(randint(1, 5)))
        return s

    #@test.it("Tests")
    def it_1():
        for _ in range(10): check(gen_string())

    return it_1()

if __name__ == '__main__':
    random_tests()