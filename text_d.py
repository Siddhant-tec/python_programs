import cv2
import pytesseract
import matplotlib.pyplot as plt


img = cv2.imread("sample.jpeg")
cv2.imshow("Image", img)
#img = cv2.resize(img, (400, 400))
#cv2.waitKey(0)
#plt.imshow("Image", img)
#plt.show()
cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()
text = pytesseract.image_to_string(img)
print(text)
