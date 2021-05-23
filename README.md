# Virtual-Pen
An open CV project that allows you to write and draw on your computer screen with different colours virtually. 

## Problem Highlights
The first problem was to detect the colour of the pen we are going to use for drawing purpose, for that I created a Python file for detecting the color with live web cam by creating a mask for a range of colors using the HSV(Hue-Saturation-Value)[https://en.wikipedia.org/wiki/HSL_and_HSV] Color space .
Next task was to find the current position of the tip of the pen and tracking its movement for drawing the line with the same colour of that of the pen.

## Achievements:
The model detects the pen and draw the shape with a good presicion , also to stop the pen we just have to cover some coloured part of the pen .

Things I have learnt by completing this project:
* Preprocessing the images using Open CV library with image Thresholding and image Segmentation.
* Applying Open CV for detecton of shapes and colour using various library like cv2.getContours() and Trackbars.

## Software and Libraries

* Open cv
* Python 2.7 NumPy
* Matplotlib
* Jupyter Notebook
