import re

part1 = re.compile("(\\d+?)\\1$")
part2 = re.compile("(\\d+?)\\1+$")
total = 0
total2 = 0

with open('input.txt', 'r') as f:
    for line in f:
        ranges = line.split(',')
        for r in ranges:
            n1, n2 = r.split("-", 2)
            for i in range(int(n1), int(n2)+1):
                if part1.match(str(i)):
                    total += i
                if part2.match(str(i)):
                    total2 += i

print(total)
print(total2)
