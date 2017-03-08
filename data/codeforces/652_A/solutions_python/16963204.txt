def input_numbers():
    return map(int, raw_input().split(' '))

def program(h1, h2, a, b):
    # let it flow

    # calculate relative distance delta
    delta = h2 - h1

    q = delta - 8*a

    # First day, a is too large, caterpillar reaches on first day itself
    if q<=0:
        return 0

    # Calculate the relative  velocity/day
    diff = 12*(a-b)

    if diff <= 0:
        return -1

    if delta - 8*a + 12*b - 12*a < 0:
        return 1

    z = (delta - 8*a + 12*b - 12*a - 1)/diff
    return z+2

def unit_tests():
    cases = [(10,30,2,1,1), (10,13,1,1,0), (1,1000,100,99,17), (1,1000,2,1,82)]
    for case in cases:
        h1, h2, a, b, answer = case
        output = program(h1, h2, a, b)
        #print "Testing: {},{},{},{}:{}".format(case)
        assert output == answer

def main():
    h1, h2 = input_numbers()
    a, b = input_numbers()
    result = program(h1, h2, a, b)
    print result

if __name__ == "__main__":
    #unit_tests()
    main()
