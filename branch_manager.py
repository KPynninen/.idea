from PIL import Image, ImageDraw
import os


# A function to check if the base numeral branch images are usable, if not, creates them. Modify to function from the
# folder /images under the folder location of the code file? Or to ask the user for the file location.
def branch_check():
    file_path = "i:/proggis/coding/idea/images/0000.png"
    if os.path.exists(file_path):
        print("Transformer ready to use.")
    else:
        print("Initializing Transformer.")
        create_branches()
        print("Transformer ready to use.")


def create_branches():
    # Create a new blank image
    width, height = 400, 400
    zero = Image.new("RGB", (width, height), 'white')
    one = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    two = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    three = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    four = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    five = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    six = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    seven = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    eight = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    nine = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Directory to save the images (change to ask user?)

    directory = "i:/proggis/coding/idea/images/"

    # Draw initial branches, iterate over mirroring them into tens, hundreds, thousands and save individually.
    # Make it an 'Initialize'-module

    # Create an ImageDraw object
    draw = ImageDraw.Draw(zero)

    # Draw the 0
    line_color = "black"
    line_width = 20
    line_coords = [(200, 10), (200, 390)]
    draw.line(line_coords, fill=line_color, width=line_width)

    # Display the image
    # zero.show()

    # filepath for saving the image with specified filename
    file_name = "0000.png"
    file_path = directory + file_name

    # Save the image to a file
    zero.save(file_path)

    # creating the branches/images for separate numbers

    # one
    draw = ImageDraw.Draw(one)
    line_coords1 = [(200, 19), (390, 19)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    file_name = "0001.png"
    file_path = directory + file_name
    one.save(file_path)

    # two
    draw = ImageDraw.Draw(two)
    line_coords1 = [(200, 149), (390, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    file_name = "0002.png"
    file_path = directory + file_name
    two.save(file_path)

    # three
    draw = ImageDraw.Draw(three)
    line_coords1 = [(205, 18), (390, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    file_name = "0003.png"
    file_path = directory + file_name
    three.save(file_path)

    # four
    draw = ImageDraw.Draw(four)
    line_coords1 = [(200, 149), (390, 22)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    file_name = "0004.png"
    file_path = directory + file_name
    four.save(file_path)

    # five
    draw = ImageDraw.Draw(five)
    line_coords1 = [(200, 19), (390, 19)]
    line_coords2 = [(200, 149), (385, 22)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    file_name = "0005.png"
    file_path = directory + file_name
    five.save(file_path)

    # six
    draw = ImageDraw.Draw(six)
    line_coords1 = [(385, 10), (385, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    file_name = "0006.png"
    file_path = directory + file_name
    six.save(file_path)

    # seven
    draw = ImageDraw.Draw(seven)
    line_coords1 = [(200, 19), (390, 19)]
    line_coords2 = [(385, 10), (385, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    file_name = "0007.png"
    file_path = directory + file_name
    seven.save(file_path)

    # eight
    draw = ImageDraw.Draw(eight)
    line_coords1 = [(200, 149), (390, 149)]
    line_coords2 = [(385, 10), (385, 159)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    file_name = "0008.png"
    file_path = directory + file_name
    eight.save(file_path)

    # nine
    draw = ImageDraw.Draw(nine)
    line_coords1 = [(200, 149), (390, 149)]
    line_coords2 = [(385, 10), (385, 159)]
    line_coords3 = [(200, 19), (390, 19)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    draw.line(line_coords3, fill=line_color, width=line_width)
    file_name = "0009.png"
    file_path = directory + file_name
    nine.save(file_path)

# A for loop to flip the basic numeral branches into tens, hundreds and thousands.

    # Looping through all the numerals, creating tens.
    for i in range(1, 10):
        input_image = Image.open(f'i:/proggis/coding/idea/images/000{i}.png')
        modified_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
        modified_image.save(f'i:/proggis/coding/idea/images/00{i}0.png')

    # Looping through all the numerals, creating hundreds.
    for i in range(1, 10):
        input_image = Image.open(f'i:/proggis/coding/idea/images/000{i}.png')
        modified_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)
        modified_image.save(f'i:/proggis/coding/idea/images/0{i}00.png')

    # Looping through all the numerals, creating thousands.
    for i in range(1, 10):
        input_image = Image.open(f'i:/proggis/coding/idea/images/0{i}00.png')
        modified_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
        modified_image.save(f'i:/proggis/coding/idea/images/{i}000.png')



