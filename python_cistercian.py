# Proggis

import branch_manager

# Cistercian transformer:
# Takes a number or series of numbers and transforms it into cistercian numerals. Larger than four digits results in
# multiple numerals, presented one after another. output as a pdf? is there a program to "read" cistercians?

# switch a number to a string, chop in to strings of four, read individual characters as numbers again to get
# corresponding cistercian "branch". cistercian "branches" as separate images compiled into a numeral?
# (0001, 0010, 0100, 1000 etc?) a way to compile/connect images? - Pillow-library "branches" without backgrounds to
# add on to | base?
# cistercian numeral as an object containing four digits/branches?

# test if there are cistercian numeral base branches present, if not, initialize with pillow, creating the branches.
# Set into its own module.

branch_manager.branch_check()


# test for the inputted string to be a number for the translation to work

# iterate over the input string with a step of 4
for i in range(0, len(input_string), 4):
    # slice the input string into sections of 4
    section = input_string[i:i+4]
    sections.append(section)  # append the section to the list

print(sections)  # output the list of sections, propably into a temp file

