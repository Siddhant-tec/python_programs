import cv2
import numpy as np

img = cv2.imread("/home/siddhant/Downloads/view1.jpeg")
img = cv2.resize(img, (720, 480))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
img_contours = sorted(img_contours, key=cv2.contourArea)
for i in img_contours:

    if cv2.contourArea(i) > 100:

        break

mask = np.zeros(img.shape[:2], np.uint8)

cv2.drawContours(mask, [i], -1, 255, -1)

new_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Image with background removed", new_img)

img2 = cv2.GaussianBlur(img1, (7, 7), 0)
img2 = cv2.Canny(img2, 100, 200)
cv2.imshow("Original", img)
#cv2.imshow("Blurred", img1)
#cv2.imshow("Edges", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
