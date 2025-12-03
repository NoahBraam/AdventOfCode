
dial = 50
pwd = 0
part2 = 0

with open('input.txt', 'r') as f:
    for line in f:
        amount = int(line[1:])
        if line[0] == 'L':
            # Reverse the dial to make this calculation easier)
            part2 += int((((100 - dial) % 100) + amount)/100)
            dial -= amount
        else:
            part2 += int((dial + amount) / 100)
            dial += amount
        dial = dial % 100
        if dial == 0:
            pwd += 1

print(pwd)
print(part2)


