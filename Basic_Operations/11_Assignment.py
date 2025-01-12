import cv2

# image_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\assignment-001-given.jpg'
image = cv2.imread('assignment-001-given.jpg')
background_label = image.copy()

cv2.rectangle(background_label, (810,85), (1265, 195), (0,0,0), -1)

blended_image = cv2.addWeighted(background_label, 0.5, image, 0.5, 0)

cv2.rectangle(blended_image, (265, 195), (990, 920), (0, 255, 0), 5)

cv2.putText(blended_image, 'RAH972U', (825,175), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

cv2.imshow("Assignment_image", blended_image)

cv2.waitKey(0)

cv2.imwrite("assignment_result.jpg", blended_image)

cv2.destroyAllWindows()