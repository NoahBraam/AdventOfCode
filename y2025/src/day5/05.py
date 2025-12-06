

def main():
    with open("input.txt", "r") as f:
        input_data = f.read().splitlines()
    fresh = set()
    total = 0
    for line in input_data:
        if "-" in line:
            (n1, n2) = line.split("-")
            fresh.add((int(n1), int(n2)))

        else:
            if line == "":
                continue
            valid = False
            for (n1, n2) in fresh:
                if int(line) >= n1 and int(line)<=n2:
                    valid = True
                    break
            if valid:
                total += 1

    print(total)
    sorted_fresh = sorted(fresh)
    max = 0
    part2 = 0
    for (n1, n2) in sorted_fresh:
        if n2 < max:
            continue
        if n1 <= max:
            n1 = max +1
        part2 += (n2 - n1) +1
        max = n2
    print(part2)





if __name__ == "__main__":
    main()
