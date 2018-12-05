def sum_all(numbers):
    r_fqs = [0, ]
    r = 0
    for number in numbers:
        r += int(number)
        r_fqs.append(r)
    return r, r_fqs


def solute(fqs):
    fs = {}
    for fq in fqs:
        if fq not in fs:
            fs[fq] = 1
        else:
            return fq
    return None


lines = open('input').readlines()
numbs = [int(line) for line in lines]
result, freqs = sum_all(numbs)

r = solute(freqs)
i = 2
while r is None:

    _, freqs = sum_all(numbs * i)
    r = solute(freqs)
    i += 1

print(r)
