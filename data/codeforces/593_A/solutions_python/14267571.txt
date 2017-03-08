__author__ = 'trunghieu11'


def solve(n, words):
    letters = set(list(''.join(x for x in words)))

    answer = 0
    for a in letters:
        for b in letters:
            total = 0
            for x in words:
                curLetters = set(list(x))
                if curLetters == {a} or curLetters == {b} or curLetters == {a, b} or curLetters == {b, a}:
                    total += len(x)
            answer = max(answer, total)
    return answer

if __name__ == '__main__':
    n = int(raw_input())
    words = []
    for i in range(n):
        words.append(raw_input())
    print solve(n, words)