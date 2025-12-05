
def isValidPos(i, j, rows, cols):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return False
    return True

def can_pickup(i, j, rows, cols, data):
    if data[i][j] != "@":
        return False
    total_tp = 0
    if isValidPos(i-1, j-1, rows, cols):
        total_tp += 1 if data[i-1][j-1] == "@" else 0
    if isValidPos(i-1, j, rows, cols):
        total_tp += 1 if data[i-1][j] == "@" else 0
    if isValidPos(i-1, j+1, rows, cols):
        total_tp += 1 if data[i-1][j+1] == "@" else 0
    if isValidPos(i, j-1, rows, cols):
        total_tp += 1 if data[i][j-1] == "@" else 0
    if isValidPos(i, j+1, rows, cols):
        total_tp += 1 if data[i][j+1] == "@" else 0
    if isValidPos(i+1, j-1, rows, cols):
        total_tp += 1 if data[i+1][j-1] == "@" else 0
    if isValidPos(i+1, j, rows, cols):
        total_tp += 1 if data[i+1][j] == "@" else 0
    if isValidPos(i+1, j+1, rows, cols):
        total_tp += 1 if data[i+1][j+1] == "@" else 0
    if total_tp >= 4:
        return False
    return True


def main():
    with open('input.txt', 'r') as f:
        input_data = f.read().splitlines()
    rows = len(input_data)
    cols = len(input_data[0])
    part1 = 0
    part2 = 0
    while True:
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if can_pickup(i, j, rows, cols, input_data):
                    to_remove.append((i,j))
        if part1 == 0:
            part1 = len(to_remove)
        part2 += len(to_remove)
        if len(to_remove) == 0:
            break
        for (i, j) in to_remove:
            input_data[i] = input_data[i][:j] + "." + input_data[i][j+1:]

    print(part1)
    print(part2)

if __name__ == "__main__":
    main()

