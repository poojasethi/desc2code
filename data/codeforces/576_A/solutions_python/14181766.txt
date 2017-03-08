__author__ = 'trunghieu11'


def find(x):
    answer = []
    for i in range(2, x):
        if i**2 >= x:
            break
        if x % i == 0:
            total = 0
            while x % i == 0:
                total += 1
                x /= i
            answer.append(i**total)
    if x > 1:
        answer.append(x)
    return answer


def solve(n):
    answer = set()
    for i in range(2, n + 1):
        divisors = find(i)
        for x in divisors:
            answer.add(x)
    return '\n'.join([str(len(answer)), ' '.join(str(x) for x in answer)])


if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)