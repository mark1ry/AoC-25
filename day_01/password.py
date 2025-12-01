def get_input(filename: str)->list:
    
    input = []
    with open(filename, "r") as file:
        for line in file:
            if line[0]=="R":
                input.append(int(line[1:]))
            elif line[0]=="L":
                input.append(-1*int(line[1:]))
            else:
                print("WARNING: Unexpected input. Neither 'L' nor 'R'!")
    
    return input

def calculate_password_1(instructions: list) -> int:
    
    safe_value = 50
    password = 0
    for element in instructions:
        safe_value += element
        while safe_value<0:
            safe_value += 100
        while safe_value>99:
            safe_value -= 100
        if safe_value==0:
            password+=1
    
    return password

def is_value_good(safe_value: int) -> bool:
    if safe_value<0 or safe_value>99:
        return False
    return True

def calculate_password_2(instructions: list) -> int:
    
    safe_value = 50
    password = 0
    for element in instructions:
        if safe_value==0 and element<0:
            password-=1
        safe_value += element
        safe_value_is_good = is_value_good(safe_value)
        while not safe_value_is_good:
            if not safe_value==100:
                password += 1
            if safe_value<0:
                safe_value += 100
            elif safe_value>99:
                safe_value -= 100
            safe_value_is_good = is_value_good(safe_value)
        if safe_value==0:
            password += 1
    return password

if __name__=="__main__":
    filename = "input.txt"

    instructions = get_input(filename)
    password = calculate_password_2(instructions)
    
    print(f"The password is {password}")