from re import finditer, sub
from collections import deque


def top_3_words(text):
    text = ' ' + sub(r"\s'+\s|^'+\s|^'+$|\s'+$|[^A-Za-z']", " ", text) + ' '
    text = sub('  ', " ", text)
    words = set(text.lower().split())
    top_occurrences = []
    words_occurrences = {}
    text = text.lower()
    for word in words:
        # occurrences = finditer(r'\s'+word+r'\s', text)
        # number_of_occurrences = len(deque(occurrences, maxlen=0))
        count = 0
        index = -1
        while 1:
            index = text.find(' ' + word + ' ', index + 1)
            if index == -1:
                break

            count += 1
        words_occurrences[word] = count
        top_occurrences.append(count)

    top_occurrences.sort(reverse=True)
    top_3_occurrences = top_occurrences[:3]
    top_3 = []
    for occurrence in top_3_occurrences:
        sorted_words = [word for word in words_occurrences if words_occurrences[word] == occurrence]
        sorted_words.sort()
        top_3.extend(sorted_words)

        if len(set(top_3)) > 3:
            break

    return list(dict.fromkeys(top_3))[:3]


from collections import Counter
import re


def top_3_words2(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w, _ in c.most_common(3)]


def top_3_words3(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]


top_3_words4 = lambda t: [w for w, c in Counter(re.findall("'*[a-z][a-z']*", t.lower())).most_common(3)]


def top_3_words_orig(text):
    top_3 = Counter(w for w in re.findall(r"[a-zA-Z']+", text.lower()) if w != "'" * len(w))
    return [w for w, _ in top_3.most_common(3)]


if __name__ == '__main__':
    print(top_3_words_orig(" '"))
    print(top_3_words_orig("#In a villag'e of La Mancha, the name of which I have no desire to call to"
                       "mind, there lived not long since one of those gentlemen that keep a lance"
                       "in the lance-rack, an old buckler, a lean hack, and a greyhound for"
                       "coursing. An olla of rather more beef than mutton, a salad on most"
                       "nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra"
                       "on Sundays, made away with three-quarters of his income."))
