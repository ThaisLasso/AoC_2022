def sum_priorities(rucksacks):
    shared_items = []

    for rucksack in rucksacks:
        shared_items.extend(find_shared_items(rucksack))
    
    print(shared_items)
    return sum([find_priority(item) for item in shared_items])

def find_priority(item):
    number_shift = 96 if item.islower() else 38
    return ord(item) - number_shift

def find_shared_items(rucksack):
    compartment_1, compartment_2 = dispose_items(rucksack)

    shared = set(item for item in compartment_2 if item in set(compartment_1))
    return shared

def dispose_items(rucksack):
    half = int(len(rucksack)/2)
    return rucksack[:half], rucksack[half:]

if __name__ == '__main__':
    inputs = open('day_3_input.txt', 'r').readlines()
    print(sum_priorities(inputs))