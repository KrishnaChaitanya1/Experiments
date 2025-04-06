import numpy as np
import cv2
import imutils

# Load Image
image = cv2.imread("C:\\Users\\kchai\\Desktop\\Task\\Input.jpg")
image_resize = cv2.resize(image, (1000, 850))
original = image_resize.copy()

# Convert the Image to HSV
image_resize = cv2.cvtColor(image_resize, cv2.COLOR_BGR2HSV)

# Limits for HSV
lower = np.array([0, 0, 0], dtype="uint8")
upper = np.array([25, 25, 25], dtype="uint8")

# Mask
acv2.imshow("Mask", mask)

# Contours
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  #cnts[0] if len(cnts) == 2 else cnts[1]

cv2.fillPoly(mask, cnts, (255, 255, 255))
result = cv2.bitwise_and(original, original, mask=mask)

cv2.imshow("Result", result)

cv2.waitKey(0)