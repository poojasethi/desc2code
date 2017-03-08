k, n, w = map(int, raw_input().strip().split())
print max(w * (w + 1)/2 * k - n, 0)
