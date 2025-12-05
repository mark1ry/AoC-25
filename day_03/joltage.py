def get_input(filename: str) -> list:
    
    input = []
    with open(filename, "r") as file:
        for line in file:
            input.append(line.strip("\n"))
    
    return input

def find_best_digit(sequence: str) -> list:
    
    temp = "0"
    temp_idx = 0
    for index, digit in enumerate(sequence):
        if int(digit)>int(temp):
            temp = digit
            temp_idx = index
    
    return temp, temp_idx

def max_joltage(battery: str, n: int) -> int:
    
    joltage = ""
    stop = (-1)*(n-1)
    start = 0
    while stop != 0:
        digit, idx = find_best_digit(sequence=battery[start:stop])
        joltage += digit
        start += idx + 1
        stop += 1
    
    joltage += find_best_digit(sequence=battery[start:])[0]
    
    return int(joltage)


if __name__ == "__main__":
    
    filename = "input.txt"
    
    batteries = get_input(filename=filename)
    
    joltages = []
    for battery in batteries:
        joltages.append(max_joltage(battery, 12))
    
    print(joltages)
    print(f"The total joltage is {sum(joltages)}")