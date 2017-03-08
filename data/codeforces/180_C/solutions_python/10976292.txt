s = raw_input()

buff = []
for char in s:
    if 65 <= ord(char) <= 65 + 26:
        buff.append(1)
    else:
        buff.append(0)
def process(buff):
    answer = len(buff)
    one_freq = 0
    zero_freq = 0
    for i in buff:
        if i == 1:
            one_freq += 1
        else:
            zero_freq += 1
    converted = 0
    forward_one = 0
    for i in range(len(buff)):
        tentative = one_freq - forward_one
        temp_cost = converted + tentative
        answer = min(answer, temp_cost)
        if buff[i] == 1:
            forward_one += 1
        else:
            converted += 1
    if buff[len(buff) - 1] == 1:
        answer = min(answer, converted)
    
    return answer

print process(buff)





