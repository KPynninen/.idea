from PIL import Image, ImageDraw
import os


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
    base = Image.new("RGB", (width, height), "white")
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
    # Make it a 'Initialize'-module

    # Create an ImageDraw object
    draw = ImageDraw.Draw(base)

    # Draw the 0
    line_color = "black"
    line_width = 20
    line_coords = [(200, 10), (200, 390)]
    draw.line(line_coords, fill=line_color, width=line_width)

    # Display the image
    # base.show()

    # filepath for saving the image with specified filename
    file_name = "0000.png"
    file_path = directory + file_name

    # Save the image to a file
    base.save(file_path)

    # creating the branches/images for separate numbers

    # one
    draw = ImageDraw.Draw(one)
    line_coords1 = [(200, 19), (390, 19)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    # one.show()
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
    # three.show()
    file_name = "0003.png"
    file_path = directory + file_name
    three.save(file_path)

    # four
    draw = ImageDraw.Draw(four)
    line_coords1 = [(200, 149), (390, 22)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    # three.show()
    file_name = "0004.png"
    file_path = directory + file_name
    four.save(file_path)

    # five
    draw = ImageDraw.Draw(five)
    line_coords1 = [(200, 19), (390, 19)]
    line_coords2 = [(200, 149), (385, 22)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    # three.show()
    file_name = "0005.png"
    file_path = directory + file_name
    five.save(file_path)

    # six
    draw = ImageDraw.Draw(six)
    line_coords1 = [(385, 10), (385, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    # three.show()
    file_name = "0006.png"
    file_path = directory + file_name
    six.save(file_path)

    # seven
    draw = ImageDraw.Draw(seven)
    line_coords1 = [(200, 19), (390, 19)]
    line_coords2 = [(385, 10), (385, 149)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    # three.show()
    file_name = "0007.png"
    file_path = directory + file_name
    seven.save(file_path)

    # eight
    draw = ImageDraw.Draw(eight)
    line_coords1 = [(200, 149), (390, 149)]
    line_coords2 = [(385, 10), (385, 159)]
    draw.line(line_coords1, fill=line_color, width=line_width)
    draw.line(line_coords2, fill=line_color, width=line_width)
    # three.show()
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
    # three.show()
    file_name = "0009.png"
    file_path = directory + file_name
    nine.save(file_path)

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
