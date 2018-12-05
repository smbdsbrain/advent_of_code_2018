import re

lines = open('input').readlines()
sqrs = []

for line in lines:
    m = re.match(r'#([0-9]{1,5}) @ ([0-9]{1,5}),([0-9]{1,5}): ([0-9]{1,5})x([0-9]{1,5})', line)
    sqrs.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))))

matrix = [[[] for j in range(10000)] for i in range(10000)]


pairs = {sqr[0]: [] for sqr in sqrs}

for sqr in sqrs:
    for i in range(sqr[1], sqr[1] + sqr[3]):
        for j in range(sqr[2], sqr[2] + sqr[4]):
            matrix[i][j].append(sqr[0])


res = 0
for i in matrix:
    for j in i:
        if len(j) > 1:
            res += 1
        for k in j:
            for h in j:
                if k != h:
                    if k not in pairs[h]:
                        pairs[h].append(k)

print(res)
for k, v in pairs.items():
    if len(v) == 0:
        print(k)
