import copy


def get_input(filename: str) -> list:
    
    ranges = []
    foods = []
    end_of_ranges = False
    with open(filename, "r") as file:
        for line in file:
            if not end_of_ranges:
                if line.strip("\n")=="":
                    end_of_ranges = True
                else:
                    temp = line.strip("\n").split("-")
                    ranges.append([int(temp[0]), int(temp[1])])
            elif end_of_ranges:
                foods.append(int(line.strip("\n")))
    return ranges, foods

def is_in_range(x: int, start: int, stop: int) -> bool:
    
    if x >= start and x <= stop:
        return True
    return False

def get_ranges(raw: list) -> list:
    
    changes = True
    while changes:
        clean = []
        changes = False
        for i in raw:
            found = False
            for index, j in enumerate(clean):
                if is_in_range(i[0], j[0], j[1]):        
                    clean[index][1] = max(j[1], i[1])
                    found = True
                    changes = True
                if is_in_range(i[1], j[0], j[1]):
                    clean[index][0] = min(j[0], i[0])
                    found = True
                    changes = True
            if not found:
                clean.append(i)
        raw = copy.deepcopy(clean)
    return clean

def food_is_good(food_id: int, ranges: list) -> bool:
    
    for j in ranges:
        if is_in_range(food_id, j[0], j[1]):
            return True
    return False

def quantity_fresh(ranges: list) -> int:
    
    total = 0
    for element in ranges:
        total += (element[1]-element[0]+1)
    return total
    
if __name__=="__main__":
    
    filename = "input.txt"
    
    raw_ranges, foods = get_input(filename=filename)
    ranges = get_ranges(raw=raw_ranges)
    
    
    reversed = ranges[::-1]
    
    ranges = get_ranges(raw=reversed)

    print(f"The total amount of fresh id's is {quantity_fresh(ranges)}")
    
    good_food_count = 0
    for food in foods:
        if food_is_good(food_id=food, ranges=ranges):
            good_food_count += 1
            
    print(f"The total amount of foods that are good is {good_food_count}")