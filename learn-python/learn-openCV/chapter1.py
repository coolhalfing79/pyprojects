from cv2 import cv2 


img = cv2.imread('image.png')

for target_list in range(3):
    cv2.imshow('output', img)
    cv2.waitKey(1000)
cv2.destroyAllWindows()
