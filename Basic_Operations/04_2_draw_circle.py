import cv2  # Import OpenCV library

image_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\lena_small.jpg'
# Read the image 'lena_small.jpg'
image = cv2.imread(image_path)

# Draw a red circle on the image
# Center coordinates: (282, 282), Radius: 94
# Color: Red (BGR format: (0, 255, 0)), Thickness: 2 pixels
cv2.circle(image, (282, 282), 94, (0, 0, 255), 2)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_circle.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()