def fully_contained_assignments(pairs):
    total = 0
    for pair in pairs: 
        range_1, range_2 = ranges(pair)
        if either_fully_contains(range_1, range_2):
            total += 1
    return total

def either_fully_contains(range_1, range_2):
    contains = lambda o, i: True if o[0] <= i[0] and i[1] <= o[1] else False
    return contains(range_1, range_2) or contains(range_2, range_1)

def ranges(pair):
    elf_1, elf_2 = pair[:-1].split(',')

    to_range = lambda elf: ([int(r) for r in elf.split('-')])
    return to_range(elf_1), to_range(elf_2)

if __name__ == '__main__':
    inputs = open('day_4_input.txt', 'r').readlines()
    print(fully_contained_assignments(inputs))