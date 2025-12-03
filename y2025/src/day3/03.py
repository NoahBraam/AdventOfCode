total = 0

with open('input.txt', 'r') as f:
    for line in f:
        largest = '0'
        second = '0'
        for c in line[:-2]:
            if int(c) > int(largest):
                largest = c
        start = line.index(largest) + 1
        for c in line[start:-1]:
            if int(c) > int(second):
                second = c
        total += int(largest + second)

print(total)
