if __name__ == '__main__':
    input()
    numbers = map(int, raw_input().split())
    ok = max([numbers.count(x) for x in set(numbers)]) <= (len(numbers)+1)/2
    print ['NO', 'YES'][ok]
