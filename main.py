# Joshua Snyder
import cv2 as cv


def Main():
    # Enter the full file name and extension for example, car.jpg
    user_img = input("Enter the file name of the picture you want to convert to sketch: ")  # Gets the img from the user

    img = cv.imread(user_img)

    Scale(img)


# Scaling the image
def Scale(img):
    bigger_img = cv.resize(img, (350, 300))
    Conversion(bigger_img)


# Converting the image
def Conversion(bigger_img):
    gray = cv.cvtColor(bigger_img, cv.COLOR_BGR2GRAY)
    inverted = cv.bitwise_not(gray)
    blurred = cv.GaussianBlur(inverted, (15, 15), sigmaX=0, sigmaY=0)
    Blend(gray, blurred)


# Lets us blend the two imgs together
def Blend(img1, img2):
    drawn_image = cv.divide(img1, 255 - img2, scale=256)
    DisplayImages(drawn_image)


# Displays the images
def DisplayImages(drawn_image):
    cv.imshow("Drawn", drawn_image)


Main()

cv.waitKey(0)
