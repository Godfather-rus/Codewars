def rot13(message):
    #return ''.join([chr(ord(char)+13) if 109 <= ord(char)+13 <= 122 else chr(ord(char)-13) if 97 <= ord(char) <= 122 else ' '
     #       for char in message])
    answer = ''
    for char in message:
        if 97 <= ord(char) <= 122:
            if ord(char) + 13 <= 122:
                answer += chr(ord(char)+13)
            else:
                answer += chr(ord(char)-13)
        elif 65 <= ord(char) <= 90:
            if ord(char) + 13 <= 90:
                answer += chr(ord(char)+13)
            else:
                answer += chr(ord(char)-13)
        else:
            answer += char
    return answer


def rot13v2(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))

    return "".join(decode(c) for c in message)


def rot13v3(message):
    import codecs
    return codecs.encode(message, 'rot_13')


if __name__ == '__main__':
    print(rot13("EBG13 rknzcyr."))