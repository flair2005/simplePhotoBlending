from SimpleGraphics import *

# Defining how pixels between the two images will be blended.
# RGB values for a single pixel in both images will be summed and divided by two
# in order to get a new RGB value.
def blend_pixel(image1, image2, x, y):
	red1, green1, blue1 = getPixel(image1, x, y)
	red2, green2, blue2 = getPixel(image2, x, y)
	# red1, green1, and blue1 are the colour values found in a single pixel within image1
	# red2, green2, and blue2 are the colour values found in a single pixel within image2
	r = (red1 + red2)/2
	g = (green1 + green2)/2
	b = (blue1 + blue2)/2
	# The return is the red, green, and blue values found in a single pixel that will be used in a new image3
	return r, g, b

# Defining how all the pixels between the two images will be blended.
def full_blend(image1, image2):
	# Getting the height and width for image1 in order to create an image3 will equal parameters
	height = getHeight(image1)
	width = getWidth(image1)
	image3 = createImage(width, height)

	# For all the pixels that make up the entire height in increments of one pixel.
	for y in range(0, height, 1):
		# For all the pixels that make up the entire width in increments of one pixel.
		for x in range(0, width, 1):
			# All the pixels in image1 and image2 based on the above parameters will be blended
			# The new blended RGB value at each pixel location will be used in an image3
			r,g,b = blend_pixel(image1, image2, x, y)
			putPixel(image3, x, y, r, g, b)

	return image3

# Defining how only the center 100px of the two images will be blended
# as well as the original images on either side of the blended piece. 
def center_blend(image1, image2):
	# Getting the height and width for image1 in order to create an image3 with equal parameters
	height = getHeight(image1)
	width = getWidth(image1)
	image3 = createImage(width, height)

	# Blending is restricted to a certain set of parameters.  
	# The parameters are designed to blend only over a range of 100px
	# Starting at 350 and ending at 450.  Below are the defined variables.
	startCenter = 350
	endCenter = 450

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 0 to 350
		for x in range(0, startCenter, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image1, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel	
	for y in range(0, height, 1):
		# For all the pixels that make up the blended center from 350 to 450.
		for x in range(startCenter, endCenter, 1):
			# All the pixels based on the parameters above will be used in an image3 (blended)
			r,g,b = blend_pixel(image1, image2, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 450 to the end of the image1 width.
		for x in range(endCenter, width, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image2, x, y)
			putPixel(image3, x, y, r, g, b)


	return image3

# Defining how only the right 100px of the two images will be blended
# as well as the original images on either side of the blended piece. 
def right_blend(image1, image2):
	# Getting the height and width for image1 in order to create an image3 with equal parameters
	height = getHeight(image1)
	width = getWidth(image1)
	image3 = createImage(width, height)

	startRight = 550
	endRight = 650

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 0 to 550
		for x in range(0, startRight, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image1, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the blended center from 550 to 650.
		for x in range(startRight, endRight, 1):
			# All the pixels based on the parameters above will be used in an image3 (blended)
			r,g,b = blend_pixel(image1, image2, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 650 to the end of the image1 width.
		for x in range(endRight, width, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image2, x, y)
			putPixel(image3, x, y, r, g, b)

	return image3

# Defining how only the left 100px of the two images will be blended
# as well as the original images on either side of the blended piece. 
def left_blend(image1, image2):	
	# Getting the height and width for image1 in order to create an image3 with equal parameters
	height = getHeight(image1)
	width = getWidth(image1)
	image3 = createImage(width, height)

	startLeft = 150
	endLeft = 250

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 0 to 150
		for x in range(0, startLeft, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image1, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the blended center from 150 to 250.
		for x in range(startLeft, endLeft, 1):
			# All the pixels based on the parameters above will be used in an image3 (blended)
			r,g,b = blend_pixel(image1, image2, x, y)
			putPixel(image3, x, y, r, g, b)

	# For all the pixels that make up the entire height in increments of one pixel
	for y in range(0, height, 1):
		# For all the pixels that make up the width from 250 to the end of the image1 width.
		for x in range(endLeft, width, 1):
			# All the pixels based on the parameters above will be used in an image3 (no blending)
			r,g,b = getPixel(image2, x, y)
			putPixel(image3, x, y, r, g, b)

	return image3

# Defining the user input, as well as a while loop to return a user prompt if the input is invalid.  
# The user will enter a value 1, 2, 3, or 4 as written in the prompt. 
def user():
	userInput = int(input("Please state how you would like to blend your two images.  Enter 1 to blend both images, 2 to blend at the center, 3 to blend at the right, or 4 to blend at the left: "))
	
	while userInput > 4 or userInput < 1:
		userInput = int(input("Non-valid input, please enter either 1, 2, 3, or 4: "))

	return userInput

# Defining the two images that will be loaded. 
def main():
	image1 = loadImage("image1.gif")
	image2 = loadImage("image2.gif")

	userSelection = user()
	# User selected a full blend of both images, the variable defined by the user input 1.
	if userSelection == 1:
		display = full_blend(image1, image2)
		drawImage(display, 0, 0)
	# User selected a center blend, the variable defined by the user input 2.
	elif userSelection == 2:
		display = center_blend(image1, image2)
		drawImage(display, 0, 0)
	# User selected a right hand blend, the variable defined by the user input 1..
	elif userSelection == 3:
		display = right_blend(image1, image2)
		drawImage(display, 0, 0)
	# User selected a left hand blend, the variable defined by the user input 1.
	elif userSelection == 4:
		display = left_blend(image1, image2)
		drawImage(display, 0, 0)
	# An else to complete the if/else statement, but will not be utilized because of the above while loop.
	else:
		print("")

main()
