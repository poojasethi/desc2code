# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input()

    if n <= 26:
        result = n - len(set(s))
    else:
        result = -1
    print(str(result))
