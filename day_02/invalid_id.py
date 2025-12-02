import numpy as np

def get_input(filename: str) -> list:
    
    input = []
    with open(filename, "r") as file:
        for line in file:
            temp = line.split(",")
            for element in temp:
                range = element.split("-")
                input.append([int(range[0]), int(range[1])])
    return input

def find_repeated(range: list, repeated_numbers: list, n: int) -> int:
    l1 = len(str(range[0]))
    l2 = len(str(range[1]))
    if l1%n==0:
        length = int(l1/n)
        temp = str(range[0])[:length]
        while int(n*temp)<=range[1] and len(temp)==length:
            if (not (int(n*temp)<range[0])) and (not (int(n*temp) in repeated_numbers)):
                repeated_numbers.append(int(n*temp))
            temp = str(int(temp)+1)

    if l1 < l2:
        repeated_numbers = find_repeated([int(pow(10, l1)), range[1]], repeated_numbers, n=n)
    
    return repeated_numbers

def find_in_range(range: list, repeated_numbers: list):
    
    l2 = len(str(range[1]))
    
    for n in np.arange(2, l2+1):
        repeated_numbers = find_repeated(range, repeated_numbers, n)
    
    return repeated_numbers
    
if __name__=="__main__":
    
    filename = "input.txt"
    input = get_input(filename=filename)
    
    repeated = []
    for element in input:
        repeated = find_in_range(element, repeated)
        
    print(f"The total sum invalid ID's is {sum(repeated)}")
