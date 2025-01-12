import cv2  # Import OpenCV library

image1_path=r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\pig.png'
image2_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\fish.png'
# Read two images of the same size
# Here, we use 'lena.jpg' twice for simplicity
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Blend the two images with equal weights (0.5 each)
blended = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

# Display the blended image in a window
cv2.imshow('Image', blended)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the blended image to a new file
cv2.imwrite('pish.png', blended)

# Close all OpenCV windows
cv2.destroyAllWindows()