# coding=utf-8
"""
D. Скобочная последовательность
ограничение по времени на тест:1 second
ограничение по памяти на тест:64 megabytes
ввод:standard input
вывод:standard output

Перед вами еще одна задача на правильные скобочные последовательности.

Напомним, что скобочная последовательность называется правильной, если путем вставки в нее символов «+» и «1» можно
получить из нее корректное математическое выражение. Например, последовательности «(())()», «()» и «(()(()))» —
правильные, в то время как «)(», «(()» и «(()))(» — нет.

Вам задан шаблон скобочной последовательности, в котором присутствуют символы «(», «)» и «?». Вам надо заменить каждый
символ «?» на скобку таким образом, чтобы получилась правильная скобочная последовательность.

Для каждого символа «?» в шаблоне известна стоимость замены его на «(» и «)». Ваша задача из всех возможных вариантов
выбрать самый дешевый вариант.
Входные данные

В первой строке входного файла записан непустой шаблон четной длины, состоящий из символов «(», «)» и «?». Его длина не
превосходит 5·104. Далее содержится m строк, где m — количество символов «?» в шаблоне. Каждая строка состоит из двух
целых чисел ai и bi (1 leai, bi ≤ 106), где ai стоимость замены i-го символа «?» на открывающуюся скобку, а bi — на
закрывающуюся.
Выходные данные

В первую строку выведите стоимость искомой последовательности. Во вторую выведите искомую последовательность.

Если решения не существует, выведите -1. Если решений несколько, выведите любое.
"""

from collections import Counter
from sys import stdin, exit


def insert(items, pos, cost):
    i = 0
    inserted = False
    for j, c in items:
        if c >= cost:
            items.insert(i, (pos, cost))
            inserted = True
            break
        i += 1
    if not inserted:
        items.append((pos, cost))


def task():
    line = list(stdin.readline().strip())
    costs = []
    for (x, y) in [(int(x), int(y)) for x, y in map(str.split, stdin.readlines())]:
        costs.append((x, y))

    if len(line) % 2 != 0:
        print -1
        exit()

    total = 0
    changes = []
    change = 0
    MAX = 10 ** 15
    for i, ch in enumerate(line):
        if ch == '?':
            l, r = costs[change]
            line[i] = '(' if l < r else ')'
            change += 1
            changes.append(abs(l - r))
            total += min(l, r)
        else:
            changes.append(MAX)

    counter = Counter(line)
    l, r = counter['('], counter[')']
    to_change = (l - r) / 2
    sorted_changes = sorted(enumerate(changes), key=lambda c: c[1])
    if to_change > len(sorted_changes):
        print -1
        exit()

    if to_change != 0:
        count = abs(to_change)
        for i, cost in sorted_changes:
            ch = line[i]
            if (to_change > 0 and ch == ')') or (to_change < 0 and ch == '('):
                continue
            line[i] = ')' if ch == '(' else '('
            if cost == MAX:
                print -1
                exit()
            total += cost
            changes[i] = -cost
            count -= 1
            if count == 0:
                break

    d = 0
    l = []
    r = []
    sorted_changes = sorted(enumerate(changes), key=lambda c: c[1])
    for i, cost in sorted_changes:
        if cost < MAX:
            if line[i] == ')':
                l.append((i, cost))
            else:
                r.append((i, cost))

    #print line
    #print changes
    #print l
    #print r

    for i, ch in enumerate(line):
        if ch == '(':
            d += 1
        else:
            d -= 1
        if d < 0:
            swaped = False
            for j, cost in l:
                if j <= i:
                    swaped = True
                    l.remove((j, cost))
                    #changes[j] = -cost
                    total += cost
                    line[j] = '('
                    #r.insert(0, (j, -cost))
                    #r.sort(key=lambda c: c[1])
                    insert(r, j, -cost)
                    break

            if not swaped:
                print -2
                exit()

            #print '%s>' % i,  ''.join(line)

            swaped = False
            for j, cost in r:
                if j > i:
                    swaped = True
                    r.remove((j, cost))
                    #changes[j] = -cost
                    total += cost
                    line[j] = ')'
                    #l.insert(0, (j, -cost))
                    #l.sort(key=lambda c: c[1])
                    insert(l, j, -cost)
                    break
            if not swaped:
                print -1
                exit()
            d += 2
            #print '%s>>' % i, ''.join(line)

    print total
    print ''.join(line)

task()