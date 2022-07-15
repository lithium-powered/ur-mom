import copy
import re

print('hello world')

operators = ['+', '-', '/', '*']

def get_parenthesis_encapsulated_string_end_index(input: str, start_index: int) -> str:
    count = 1
    output = ''
    if input[start_index:start_index+1] != '(':
        raise Exception("Invalid parenthesis!")
    start_index += 1
    while count > 0:
        char = input[start_index:start_index+1]
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        start_index += 1
        if count == 0:
            return start_index
        if start_index > len(input) + 1:
            raise Exception("Invalid parenthesis!")
    return -1

def convert_alphanumeric_to_decimal(input: str) -> int:
    numwords = {}
    units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):    numwords[word] = (1, idx)
    for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def convert_roman_to_decimal(input: str) -> int:
    def value(r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1

    res = 0
    i = 0
    while (i < len(str)):
        # Getting value of symbol s[i]
        s1 = value(str[i])
        if (i + 1 < len(str)):
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
            # Comparing both values
            if (s1 >= s2):
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res


def calc_power(input_array) -> int:
    return input_array[0] ** input_array[1]


def calc(input: str) -> int:
    input = input.lower()
    # for i in range(0, len(input)):
    #     char = input[i:i+1]
    #     if char == '(':
    #         if i > 2 and input[i-3:i-1] == "pow":
    #             calc_pow(get_parenthesis_encapsulated_string(input, i).split(','))
    #         else:
    #             string = get_parenthesis_encapsulated_string(input, i).split(','))

    return 0