def sum_priorities(rucksacks):
    shared_items = []

    groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]
    for group in groups:
        shared_items.extend(find_shared_items(group))

    return sum([find_priority(item) for item in shared_items])

def find_priority(item):
    if item == '\n': return 0
    number_shift = 96 if item.islower() else 38
    return ord(item) - number_shift

def find_shared_items(group):
    rucksack_1, rucksack_2, rucksack_3 = group
    shared = set(item for item in rucksack_1 if item in set(rucksack_2) and item in set(rucksack_3))
    return shared

if __name__ == '__main__':
    inputs = open('day_3_input.txt', 'r').readlines()
    print(sum_priorities(inputs))