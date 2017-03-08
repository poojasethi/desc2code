from itertools import groupby

def main():
    n = int(raw_input())
    arr = sorted(map(int, raw_input().split()))
    ma = sorted([len(list(it)) for _, it in groupby(arr)])
    ans = 0
    for i, (l, x) in enumerate(zip([0] + ma, ma)):
        ans += (len(ma) - i - 1) * (x - l)
    print ans

main()


# 01:01   756
