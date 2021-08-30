import re
import sys


def valid_pattern(password, signal, value, what):
    pass_len = 0

    if what == 'LEN':
        pass_len = len(password)
    if what == 'SPECIALS':
        pass_len = len(re.sub(r"[a-zA-Z0-9]", "", password))
    if what == 'NUMBERS':
        pass_len = len(re.sub(r"\D", "", password))
    if what == 'LETTERS':
        pass_len = len(re.sub(r"[^a-zA-Z]", "", password))

    validation = False

    if signal == '=':
        validation = pass_len == value
    if signal == '<':
        validation = pass_len < value
    if signal == '>':
        validation = pass_len > value

    return validation


def valid_pass(password, req):
    validation = True

    for x in req:

        validation = validation and valid_pattern(password, x[1], int(x[2]), x[0])
        if not validation:
            return False

    return validation


def main(password, rules):
    ret = valid_pass(password,  eval(rules) if isinstance(rules, str) else rules)
    print(ret)
    return ret


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
