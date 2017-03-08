
def main():
    nums = []
    for x in xrange(64):
        ones = '1'*x
        for y in xrange(x + 1):
            # print '1' + ones[:y] + '0' + ones[y:]
            nums.append(int('1' + ones[:y] + '0' + ones[y:], 2))
    a, b = map(int, raw_input().split())
    count = 0
    for x in nums:
        if a <= x <= b:
            count += 1
    print count

main()
