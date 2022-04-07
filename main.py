import cv2
import os

file = 'test.jpg'
path = os.path.abspath(file)
windowTitle = 'wow panes'
readCvImage = cv2.imread(file, 1)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

