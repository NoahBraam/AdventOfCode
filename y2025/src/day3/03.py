
def main():
    num_batteries = int(input())
    max_joltages = []
    with open('input.txt', 'r') as f:
        input_data = f.read().splitlines()
    
    for bank in input_data:
        bank_len = len(bank)
        bank_joltages = [int(joltage) for joltage in bank]
        remaining = num_batteries
        batteries_enabled = []
        i = -1 
    
        while remaining > 0:
            search_slice = bank_joltages[i+1 : bank_len - remaining + 1]
            battery_joltage = max(search_slice)
            
            i = bank_joltages.index(battery_joltage, i+1)
            
            batteries_enabled.append(battery_joltage)
            batteries_remaining -= 1

        max_joltages.append(int("".join(str(battery) for battery in batteries_enabled)))
    print(sum(max_joltages))


if __name__ == "__main__":
    main()
