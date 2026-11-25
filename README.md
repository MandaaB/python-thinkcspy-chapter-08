# Image Generation Exercises (ThinkCS Python Chapter 8)

This project is a set of programming exercises based on Chapters 7 and 8 of "How to Think Like a Computer Scientist: Learning with Python." The focus is on using **loops** and **if statements** to manipulate images at the pixel level.

## Background

The exercises guide you through creating and modifying images using a simple image library. You'll use **nested loops** to visit every pixel in an image and **if statements** to decide how each pixel should be colored. This is a practical way to understand how computers process images and how conditional logic and iteration work together in programming.

## Exercises

- **Red Image:** Fill an entire image with red pixels - this is already done for you.  
- **Random Noise:** Fill an image with random black and white pixels.
- **White Line:** Draw a single white line across a black image, location is based on a parameter.
- **Alternate Lines:** Create an image with white horizontal lines on a black image, gap between white lines is provided by a parameter.
- **Steganography Decoder:** Reveal a hidden image by checking if the red channel of each pixel is odd or even.

## Learning Goals

- Practice using `for` loops to iterate over image coordinates.
- Use `if` statements to make decisions about pixel color.
- Understand how images are represented as grids of pixels.
- See how simple logic can create interesting visual effects.

## How to Run

1. In main.py, you will find the code for each exercise.  Your job is to complete each of the functions (`draw_white_line`, `draw_alternate_lines`, `draw_random_noise`, and `decode_steganography`) to generate the desired images.  
   The `draw_red_image` function is already complete. and acts as an example of how to manipulate pixels in an image.
2. As in the previous challenges, each of the function is part of a larger system and is called by the user interface.  Run `python main.py` to launch the UI in the terminal.
3. Use various options to call each of the functions.

Here's a short video on how to run the GUI and what the solution should look like (except for the last question).  <a href="https://youtu.be/remNR4jF-Rg" target="_blank">https://youtu.be/remNR4jF-Rg</a>

This challenge is a hands-on way to build your confidence with **loops** and **if statements**—two of the most important tools in any programmer's toolkit!

## Submission

After completing the exercises, run ```pytest``` to ensure all tests pass. Then, submit your code by running the following command in your terminal:

```bash
git add -A
git commit -m 'submit'
git push
```

