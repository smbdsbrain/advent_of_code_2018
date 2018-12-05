def differ_chars(s1, s2):
    if len(s1) != len(s2):
        raise ValueError('line size a diffs')

    n = 0
    for i, c in enumerate(s1):
        if c != s2[i]:
            n += 1
    return n


lines = open('input').readlines()

result = {
    2: 0,
    3: 0,
}

for line in lines:
    chars = {}
    for c in line:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    two, three = False, False
    for k, v in chars.items():
        if v == 2:
            two = True

        if v == 3:
            three = True

    if two:
        result[2] += 1

    if three:
        result[3] += 1

print(result[2] * result[3])


for line in lines:
    for line2 in lines:

        dc = differ_chars(line, line2)
        if dc == 1:
            print(f'{line} {line2}')
