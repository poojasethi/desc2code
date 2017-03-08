'''
given an array of integers, given query li, ri, check a subsegment of the array is a ladder or not
a ladder is a sequence of integers b1<= b2 <= ... <= bx >= bx+1 >= ... >= bk
'''
n, m = map(int, raw_input().split())
nums = list(map(int, raw_input().split()))
left = [0] * n
right = [0] * n
right[n-1] = n - 1

for i in xrange(1, n):
    if nums[i] <= nums[i - 1]:
        left[i] = left[i - 1]
    else:
        left[i] = i
    if nums[n - i] >= nums[n - i - 1]:
        right[n - i - 1] = right[n - i]
    else:
        right[n - i - 1] = n - i - 1

for i in xrange(m):
    l, r = map(int, raw_input().split())
    if (left[r -1] <= right[l - 1]):
        print "Yes"
    else:
        print "No"