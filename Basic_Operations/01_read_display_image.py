import cv2  # Import OpenCV library

# Read the image file 'lena.jpg'
# Ensure 'lena.jpg' is in the same directory as this script
image_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\lena_small.jpg'
image = cv2.imread(image_path)

# Display the image in a new window named 'Image'
cv2.imshow('Image Window', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
