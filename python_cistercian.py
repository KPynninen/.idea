# Proggis

import branch_manager

# Cistercian transformer:
# Takes a number or series of numbers and transforms it into cistercian numerals. Larger than four digits results in
# multiple numerals, presented one after another. output as a pdf? is there a program to "read" cistercians?

# switch a number to a string, chop in to strings of four, read individual characters as numbers again to get
# corresponding cistercian "branch"?
# cistercian "branches" as separate images compiled into a numeral? (0001, 0010, 0100, 1000 etc?) a way to compile/connect images? - Pillow-library "branches" without backgrounds to add on to | base? Through pillow merge with alpha channel transparency. X
# cistercian numeral as an object containing four digits/branches?

# test if there are cistercian numeral base branches present, if not, initialize with pillow, creating the branches. X
# modify to be portable, user input for working folder etc

branch_manager.branch_check()


# test for the inputted string to be a number for the translation to work
# input also from a file?

# iterate over the input string with a step of 4
#for i in range(0, len(input_string), 4):
#    # slice the input string into sections of 4
#    section = input_string[i:i+4]
#    sections.append(section)  # append the section to the list
#
#print(sections)  # output the list of sections, propably into a temp file

# combining images with alpha channel transparency

# image1 = Image.open("i:/proggis/coding/idea/images/0000.png")
# image2 = Image.open("i:/proggis/coding/idea/images/0009.png")

# width, height = image1.size  # using the first images size for the combined one
# merged_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Paste the opened images onto the merged image
# merged_image.paste(image1, (0, 0))
# merged_image.paste(image2, (0, 0), image2)

# merged_image.show()

# Save the merged image to a file
# merged_image.save('i:/proggis/coding/idea/images/test.png')
