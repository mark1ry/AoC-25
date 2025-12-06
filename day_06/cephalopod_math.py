import numpy as np

def get_input(filename: str) -> list:
    
    input = []
    
    with open(filename, "r") as file:
        for line in file:
            temp = []
            for digit in line.strip("\n"):
                temp.append(digit)
            temp = temp[::-1]
            input.append(temp)
    
    input = np.array(input)
    numbers = list(input[0])
    
    for line in input[1:-1,:]:
        for j, element in np.ndenumerate(line):
            temp = numbers[j[0]]
            numbers[j[0]] = temp + element
    
    numbers = [element.replace(" ", "") for element in numbers]
    numbers.append('')
    final = []
    
    i = 0
    while i<len(numbers):
        temp = []
        while numbers[i]!='':
            temp.append(int(numbers[i]))
            i += 1
        final.append(temp)
        i += 1    
    
    
    operations = []
    for element in input[-1]:
        if element != " ":
            operations.append(element)
    
    
    return final, operations

def do_calculations(numbers: list, operation: str) -> int:
    
    if operation=="+":
        return sum(numbers)
    
    if operation=="*":
        temp = 1
        for element in numbers:
            temp *= element
        return temp

def get_results(numbers: list, operations: list) -> list:
    
    results = []
    for index in range(len(operations)):
        results.append(do_calculations(numbers[index], operations[index]))
    
    return results


if __name__=="__main__":
    
    filename = "input.txt"
    numbers, operations = get_input(filename=filename)
    
    results = get_results(numbers, operations)
    
    print(f"The total sum of the values is {sum(results)}")