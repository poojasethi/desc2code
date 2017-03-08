
def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret


def main():
    n, k = read_array(int)
    ns = read_array(int)
    segment_ksum = [0] * n
    segment_ksum[0] = sum(ns[:k])
    for i in xrange(1, n-k+1):
        segment_ksum[i] = segment_ksum[i-1] - ns[i-1] + ns[i+k-1]
    max_segment_ksum = [0] * n
    max_segment_ksum[0] = segment_ksum[0]
    max_id = [-1] * n
    max_id[0] = 0
    for i in xrange(1, n-k+1):
        max_segment_ksum[i] = max(max_segment_ksum[i-1], segment_ksum[i])
        if segment_ksum[i] > max_segment_ksum[i-1]:
            max_id[i] = i
        else:
            max_id[i] = max_id[i-1]

    a, b = None, None
    best_ans = -1
    for i in xrange(k, n-k+1):
        _a = max_id[i-k]
        _b = i
        new_ans = max_segment_ksum[i-k] + segment_ksum[i]
        if new_ans > best_ans:
            best_ans = new_ans
            a, b = _a, _b

    print a+1, b+1


main()
