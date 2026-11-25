import image
import random


"""
The following function is simply an example of how to create a new image
using the image library from the text.  Here we create an image
of width and height and set every pixel to red using a nested loop
as outline in chatper 8.11

"""
def createRedImage(width, height):

    im = image.EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            im.setPixel(x, y, image.Pixel(255, 0, 0))

    return im

"""

Exercise 1

Using the random.random() function, create an image called random.gif where
each pixel has a 50% chance of being white or black

"""

def createRandomNoise(width, height):
    im = image.EmptyImage(width, height)

    for x in range(width):
        for y in range(height):
            # Replace pass with your random noise logic
            pass

    return im


"""
Exercise 2

Create a image called white_line.gif where the entire image
is black with a single white line.  The line should be line_num pixels from the 
top of the image and the width is across the entire image.  The line should be 1 pixel thick.  
For example, if line_num is 10, then the line should be on the 10th row of pixels from the 
top of the image.

"""
def createWhiteLine(line_num, width, height):
    im = image.EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            # Replace pass with your white line logic
            pass

    return im


"""
Exercise 3

Create an image called alternate_lines.gif where we have 
a black image with alternating white lines.  The gap variable is 
the number of pixels between each white line.

"""

def createAlternateLines(gap, width, height):
    im = image.EmptyImage(width, height)

    for x in range(width):
        for y in range(height):
            # Replace pass with your alternate lines logic
            pass

    return im


"""
Exercise 4

Steganography is the practice of concealing a file, message, image, or video within another 
file, message, image, or video. 

The file encoded_image.gif looks normal, but we actually hid a secret black and white
image inside the red channel.  Implement the following algorithm:

 - The secret image is the same width and size of encoded.gif
 - Use our nested loop to process each pixel:
     - If the red channel is odd, turn the resulting pixel on the new image to black
     - if the red channel is even, turn the resulting pixel on the new image to red

"""

def decodeImage():
    secret = image.Image("encoded.png")    

    for x in range(secret.width):
        for y in range(secret.height):
            # Replace pass with your decoding logic
            pass

    return secret


#---- DO NOT EDIT BELOW THIS LINE --
# Here a simple CLI to test each of your functions:


def cli():

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    width = 300
    height = 300

    while True:
        # Start with a menu to select which function to run
        print("Select a function to run:\n")
        print("1. Create Random Noise Image")
        print("2. Create White Line Image")
        print("3. Create Alternate Lines Image")
        print("4. Decode Image")
        print("5. Create Demo Animation Combining random noise, white line, and alternate lines")
        print("Q: Quit\n")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            im = createRandomNoise(width, height)
            print("Creating random noise image...")
            im.save("random.gif")
            print(f"\n{GREEN}Random noise image saved as {YELLOW}random.gif{RESET}\n")
        elif choice == "2":
            line_num = int(input("Enter the line number for the white line (0 to {}): ".format(height - 1)))
            im = createWhiteLine(line_num, width, height)
            print("Creating white line image...")
            im.save("white_line.gif")
            print(f"\n{GREEN}White line image saved as {YELLOW}white_line.gif{RESET}\n")
        elif choice == "3":
            gap = int(input("Enter the gap between white lines (number of pixels): "))  
            im = createAlternateLines(gap, width, height)
            print("Creating alternate lines image...")
            im.save("alternate_lines.gif")
            print(f"\n{GREEN}Alternate lines image saved as {YELLOW}alternate_lines.gif{RESET}\n")
        elif choice == "4":
            secret = decodeImage()
            print("Decoding image...")
            secret.save("decoded_image.gif")
            print(f"\n{GREEN}Decoded image saved as {YELLOW}decoded_image.gif{RESET}\n")
        elif choice == "5":
            print("Creating animation of 1 second of random noise, \n" 
            + "    followed by 2 seconds of white line, \n" 
            + "    followed by 2 seconds of alternate lines. \n"
            + "    This may take a moment to generate...")
            frames = []
            # Create 30 frames of random noise (assuming 30 frames per second for a 1 second animation)
            for i in range(30):
                frames.append(createRandomNoise(width, height))
            for i in range(60):
                frames.append(createWhiteLine(i * 5 % height, width, height))
            for i in range(60):
                frames.append(createAlternateLines(i % height, width, height))
            image.saveGif("demo_animation.gif", frames, duration=30)
            print(f"\n{GREEN}Demo animation saved as {YELLOW}demo_animation.gif{RESET}\n")
        elif choice.upper() == "Q":
            print(f"\n{GREEN}Exiting program. Goodbye!{RESET}\n")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    cli()