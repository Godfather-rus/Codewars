ROMAN_NUMERALS = (('I','V'),('X','L'),('C','D'),('M',))


class RomanNumerals:

    @staticmethod
    def to_roman(val : int) -> str:
        valstr = str(val)
        index = len(valstr)-1
        answer = ''
        for digit in valstr:
            digit = int(digit)
            if digit > 3:
                if digit > 8:
                    answer += ROMAN_NUMERALS[index][0] * (10-digit) + ROMAN_NUMERALS[index+1][0]
                elif digit > 4:
                    answer += ROMAN_NUMERALS[index][1] + ROMAN_NUMERALS[index][0] * (digit - 5)
                else:
                    answer += ROMAN_NUMERALS[index][0] * (5 - digit) + ROMAN_NUMERALS[index][1]
            else:
                answer += ROMAN_NUMERALS[index][0] * digit
            index -= 1

        return answer

    @staticmethod
    def from_roman(roman_num : str) -> int:
        answer = 0
        position = 0
        prev_is_big_number = True
        prev_digit = 0
        for char in roman_num:
            for i in range(len(ROMAN_NUMERALS)):
                if char in ROMAN_NUMERALS[i]:
                    digit = 0
                    is_big_number = ROMAN_NUMERALS[i].index(char) == 1
                    if is_big_number:
                        digit = 5 * (10 ** i)
                        if i > position or (i == position and not prev_is_big_number):
                            answer += digit - prev_digit * 2
                            prev_digit = digit
                        else:
                            answer += digit
                            prev_digit = digit

                        prev_is_big_number = True
                    else:
                        digit = 1 * (10 ** i)
                        if i > position:
                            answer += digit - prev_digit * 2
                            prev_digit = digit
                        else:
                            answer += digit
                            prev_digit = digit

                        prev_is_big_number = False

                    position = i
                    break



        return answer


from collections import OrderedDict
import re


ROMAN_NUMERALS = OrderedDict([
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
])

DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]

ROMAN_RE = '|'.join(ROMAN_NUMERALS)


class RomanNumerals(object):
    @staticmethod
    def from_roman(roman):
        return sum(ROMAN_NUMERALS[d] for d in re.findall(ROMAN_RE, roman))

    @staticmethod
    def to_roman(decimal):
        result = []
        for number, roman in DECIMAL_TO_ROMAN:
            while decimal >= number:
                decimal -= number
                result.append(roman)
        return ''.join(result)


if __name__ == '__main__':
    print(RomanNumerals.to_roman(99))
    print(RomanNumerals.from_roman('MMVIII'))

