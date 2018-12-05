from progress.bar import Bar
from string import ascii_lowercase

def remove_polymer_units(polymer_string, start_index):
    return polymer_string[:start_index]+polymer[start_index+2:]

# read input
polymer = open('day5/day5-input.txt', 'r').read()
polymer_index=0
bar = Bar('Processing Reactions: ', max=len(polymer))

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

# output the final length (subtracting 1 to remove \n character)
print("Final Polymer Length: %d" % (len(polymer)-1))