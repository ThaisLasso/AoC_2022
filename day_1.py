#!/usr/bin/python3

def find_biggest_inventory(inputs):
    biggest_inventory = elf_calories = 0
    for cal in inputs:
        if cal != '\n': elf_calories += int(cal)
        else:
            if elf_calories > biggest_inventory:
                biggest_inventory = elf_calories
            elf_calories = 0
    return biggest_inventory

if __name__ == '__main__':
    inputs = open('day_1_input.txt', 'r').readlines()
    print(find_biggest_inventory(inputs))