import sys


cache = {}

indent = 0

def indentWrapper(func):
    def indentFunc(*args, **kwargs):
        global indent
        indent += 1
        ret = func(*args, **kwargs)
        indent -= 1
        return ret
    return indentFunc

def l(*args):
    return
    sys.stdout.write(" " * (indent - 1) * 4)
    for x in args:
        sys.stdout.write(str(x))
        sys.stdout.write(" ")
    sys.stdout.write("\n")

@indentWrapper
def getCount(infantry, knights, currentInfantryInRow, currentKnightsInRow, maxInfantryInRow, maxKnightsInRow):

    l("count for: ", (infantry, knights, currentInfantryInRow, currentKnightsInRow))

    if (infantry, knights, currentInfantryInRow, currentKnightsInRow) in cache:
        return cache[(infantry, knights, currentInfantryInRow, currentKnightsInRow)]

    if infantry + knights == 0:
        # l("infantry + knights == 0")
        cache[(infantry, knights, currentInfantryInRow, currentKnightsInRow)] = 1
        l("return 1")
        return 1

    # test infantry
    countIfInfantry = 0
    if infantry > 0 and currentInfantryInRow > 0:
        l("I")
        countIfInfantry = getCount(infantry - 1, knights, currentInfantryInRow - 1, maxKnightsInRow, maxInfantryInRow, maxKnightsInRow)

    # test knights
    countIfKnight = 0
    if knights > 0 and currentKnightsInRow > 0:
        l("K")
        countIfKnight = getCount(infantry, knights - 1, maxInfantryInRow, currentKnightsInRow - 1, maxInfantryInRow, maxKnightsInRow)

    l(countIfInfantry, countIfKnight)

    cache[(infantry, knights, currentInfantryInRow, currentKnightsInRow)] = countIfInfantry + countIfKnight

    return (countIfInfantry + countIfKnight) % 100000000

infantry, knights, maxInfantryInRow, maxKnightsInRow = [int(x) for x in raw_input().split()]

print getCount(infantry, knights, maxInfantryInRow, maxKnightsInRow, maxInfantryInRow, maxKnightsInRow)