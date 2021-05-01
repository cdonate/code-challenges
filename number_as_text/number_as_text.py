zero_to_nine = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

teens = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

two_digits = {
    20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

magnetude_map = {
    1000000000000: 'trillion', 1000000000: 'billion', 1000000: 'million', 1000: 'thousand', 100: 'hundred'
}


def get_one_digit(number, result):
    result.append(zero_to_nine[number])


def get_two_digits(number, result):
    if number < 20:
        result.append(teens[number])
        return

    remainder = number % 10

    result.append(two_digits[number - remainder])
    if remainder != 0:
        result.append(zero_to_nine[remainder])


def get_three_digits(number, result):
    result.extend(number_as_text(number))


def get_notation(number):
    number_of_digits = 10 ** (len(str(number)) - 1)

    for digits, notation in magnetude_map.items():
        if number_of_digits < digits:
            continue
        return digits, notation
    return 1, None


length_parser = {
    1: get_one_digit,
    2: get_two_digits,
    3: get_three_digits
}


def number_as_text(number):
    result = list()

    if number == 0:
        result.append(zero_to_nine[number])
        return result

    while number > 0:
        digits, magnetude = get_notation(number)

        if digits < 100 and len(result) > 0:
            result.append('and')

        current = int(number / digits)
        length_parser[len(str(current))](current, result)

        if magnetude is not None:
            result.append(magnetude)
            number -= current*digits
            continue
        break
    return result


if __name__ == '__main__':

    print(f'             0: {" ".join(number_as_text(0))}')
    print(f'            11: {" ".join(number_as_text(11))}')
    print(f'           222: {" ".join(number_as_text(222))}')
    print(f'          3333: {" ".join(number_as_text(3333))}')
    print(f'         44444: {" ".join(number_as_text(44444))}')
    print(f'        555555: {" ".join(number_as_text(555555))}')
    print(f'       6666666: {" ".join(number_as_text(1666666))}')
    print(f'      77777777: {" ".join(number_as_text(77777777))}')
    print(f'     888888888: {" ".join(number_as_text(888888888))}')
    print(f'    9999999999: {" ".join(number_as_text(9999999999))}')
    print(f'  101010101010: {" ".join(number_as_text(101010101010))}')
    print(f' 1111111111111: {" ".join(number_as_text(1111111111111))}')
    print(f'12121212121212: {" ".join(number_as_text(12121212121212))}')

    print(f'      310510: {" ".join(number_as_text(310510))}')
    print(f'104382426112: {" ".join(number_as_text(104382426112))}')
