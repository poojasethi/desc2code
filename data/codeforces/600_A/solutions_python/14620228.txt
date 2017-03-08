import re


def number_char(words):
    numbers = []
    chars = []

    for word in re.split('[,|;]', words):
        if word.isdigit() and len(word) == len(str(int(word))):
            numbers.append(word)
        else:
            chars.append(word)

    return ('"{0}"'.format(','.join(numbers)) if len(numbers) else '-',
            '"{0}"'.format(','.join(chars)) if len(chars) else '-')

if __name__ == '__main__':
    words = raw_input()
    numbers, chars = number_char(words)
    print numbers
    print chars
