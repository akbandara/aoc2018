from progress.bar import Bar
from string import ascii_lowercase

def remove_polymer_units(polymer_string, start_index):
    return polymer_string[:start_index]+polymer[start_index+2:]

# read input
base_polymer = open('day5/day5-input.txt', 'r').read()

# variables for keeping track of the shortest polymer found
shortest_polymer = len(base_polymer)
fixed_unit = ''

# iterate through the lower case ascii characters, each time removing the 'test_unit' from the base polymer
for test_unit in ascii_lowercase:
    polymer = base_polymer.replace(test_unit, '').replace(test_unit.upper(), '')
    bar = Bar("Processing Reactions: Fixed %s" % test_unit, max=len(polymer))
    polymer_index=0
    
    # fully react the polymer be comparing adjacent pairs and removing if reaction condtions met
    while (polymer[polymer_index+1]!='\n'):
        if (str(polymer[polymer_index]).isupper() & str(polymer[polymer_index+1]).islower()):
            if (str(polymer[polymer_index])==str(polymer[polymer_index+1]).upper()):
                polymer = remove_polymer_units(polymer, polymer_index)
                polymer_index = polymer_index-1
            else:
                polymer_index = polymer_index +1
        elif (str(polymer[polymer_index]).islower() & str(polymer[polymer_index+1]).isupper()):
            if (str(polymer[polymer_index])==str(polymer[polymer_index+1]).lower()):
                polymer = remove_polymer_units(polymer, polymer_index)
                polymer_index = polymer_index-1
            else:
                polymer_index = polymer_index +1
        else:
            polymer_index = polymer_index + 1
        bar.next()
    bar.finish()

    # check if resulting polymey is the shortest thus far and update variables if needed
    if (shortest_polymer > (len(polymer)-1)):
        shortest_polymer = len(polymer)-1
        fixed_unit = test_unit
        print("Shortest Polymer Length: %d | Unit = %s" % (shortest_polymer, fixed_unit))
