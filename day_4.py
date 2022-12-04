def overlapping_assignments(pairs):
    total = 0
    for pair in pairs: 
        range_1, range_2 = ranges(pair)
        if either_overlaps(range_1, range_2):
            total += 1
    return total

def either_overlaps(range_1, range_2):
    in_interval = lambda n, i: True if n >= i[0] and n <= i[1] else False
    overlaps = lambda i1, i2: True if in_interval(i1[0], i2) or in_interval(i1[1], i2) else False
    return overlaps(range_1, range_2) or overlaps(range_2, range_1)

def ranges(pair):
    elf_1, elf_2 = pair[:-1].split(',')

    to_range = lambda elf: ([int(r) for r in elf.split('-')])
    return to_range(elf_1), to_range(elf_2)

if __name__ == '__main__':
    inputs = open('day_4_input.txt', 'r').readlines()
    print(overlapping_assignments(inputs))