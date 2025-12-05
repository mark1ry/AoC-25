import copy

def get_input(filename: str) -> list:
    
    input = []
    with open(filename, "r") as file:
        for line in file:
            temp = []
            for digit in line.strip("\n"):
                if digit==".":
                    temp.append(0)
                if digit=="@":
                    temp.append(1)
            input.append(temp)
        
    return input

def is_forkable(map: list, idx_x: int, idx_y: int) -> bool:
    
    len_y = len(map)
    len_x = len(map[0])
    
    top_edge = False
    bottom_edge = False
    left_edge = False
    right_edge = False
    
    if idx_y==0:
        top_edge = True
    if idx_y==(len_y-1):
        bottom_edge = True
    if idx_x==0:
        left_edge = True
    if idx_x==(len_x-1):
        right_edge = True
    
    adjacent_rolls = 0
    if (not top_edge) and (not left_edge):
        adjacent_rolls += map[idx_y-1][idx_x-1]
    if not top_edge:
        adjacent_rolls += map[idx_y-1][idx_x]
    if (not top_edge) and (not right_edge):
        adjacent_rolls += map[idx_y-1][idx_x+1]
    if not right_edge:
        adjacent_rolls += map[idx_y][idx_x+1]
    if (not bottom_edge) and (not right_edge):
        adjacent_rolls += map[idx_y+1][idx_x+1]
    if not bottom_edge:
        adjacent_rolls += map[idx_y+1][idx_x]
    if (not bottom_edge) and (not left_edge):
        adjacent_rolls += map[idx_y+1][idx_x-1]
    if not left_edge:
        adjacent_rolls += map[idx_y][idx_x-1]
        
    if adjacent_rolls<4:
        return True
    return False
    

def count_forkable_rolls(map: list) -> list:
    
    forkable_rolls = []
    rolls_removed_in_run = 1
    temp = copy.deepcopy(map)
    
    while rolls_removed_in_run>0:
        rolls_removed_in_run = 0
        for idx_y, file in enumerate(map):
            for idx_x, element in enumerate(file):
                if element:
                    forkable = is_forkable(map, idx_x, idx_y)
                    if forkable:
                        rolls_removed_in_run += 1
                        temp[idx_y][idx_x] = 0
        forkable_rolls.append(rolls_removed_in_run)
        map = copy.deepcopy(temp)
    return forkable_rolls

if __name__ == "__main__":
    
    filename = "input.txt"
    map = get_input(filename)
    
    forkable = count_forkable_rolls(map=map)
    
    print(f"The amount of rolls accessable by fork is {sum(forkable)}")