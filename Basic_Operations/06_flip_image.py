import cv2  # Import OpenCV library

image_path = r'C:\Users\user\Documents\computer-vision\OpenCV-Masterclass-main\OpenCV-Masterclass-main\Basic_Operations\lena_small.jpg'
# Read the image 'lena_small.jpg'
image = cv2.imread(image_path)

# Flip the image horizontally (1 = horizontal flip)
flipped_image = cv2.flip(image, 100)

# Display the flipped image in a window
cv2.imshow('Image', flipped_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the flipped image to a new file
cv2.imwrite('lena_flipped.jpg', flipped_image)

# Close all OpenCV windows
cv2.destroyAllWindows()