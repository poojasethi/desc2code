total = input()
data_list = sorted(map(int, raw_input().split()))

print 1, data_list[0]

if data_list[-1] > 0:
    print 1, data_list[-1]
    print len(data_list) - 2, ' '.join(str(number) for number in data_list[1:-1])
else:
    print 2, data_list[1], data_list[2]
    print len(data_list) - 3, ' '.join(str(number) for number in data_list[3:])
