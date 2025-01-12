import cv2  # Import OpenCV library


image_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\lena_small.jpg'
# Read the original image 'lena.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the image in a new window named 'Image'
cv2.imshow('Image', gray_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_gray.jpg', gray_image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()