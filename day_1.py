#!/usr/bin/python3

def update_inventories(biggest_inventories, elf_calories):
    biggest_inventories.sort()
    if elf_calories > biggest_inventories[0]:
        biggest_inventories[0] = elf_calories
    return biggest_inventories

def find_biggest_inventories(inputs):
    biggest_inventories = [0, 0, 0]
    elf_calories = 0
    for cal in inputs:
        if cal != '\n': 
            elf_calories += int(cal)
        else: 
            biggest_inventories = update_inventories(biggest_inventories, elf_calories)
            elf_calories = 0
    
    return sum(biggest_inventories)

if __name__ == '__main__':
    inputs = open('day_1_input.txt', 'r').readlines()
    print(find_biggest_inventories(inputs))