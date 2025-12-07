def main():
    with open("input.txt", "r") as f:
        input_data = f.read().splitlines()

    numbers = []
    operation = []
    part1 = 0
    for i in range(len(input_data)):
        if i == len(input_data) - 1:
            operation = [opts for opts in input_data[i].split(" ") if opts != ""]
        else:
            numbers.append([num for num in input_data[i].split(" ") if num != ""])


    for i in range(len(operation)):
        total = 0
        if operation[i] == "*":
            total = 1

        for j in range(len(numbers)):
            if operation[i] == "*":
                total *= int(numbers[j][i])
            elif operation[i] == "+":
                total += int(numbers[j][i])
        part1 += total
    print(part1)

    part2 = 0
    for i in range(len(operation)):
        total = 0
        if operation[i] == "*":
            total = 1



if __name__ == "__main__":
    main()
