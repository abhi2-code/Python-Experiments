import cv2

# Use raw string (r"") to avoid escape character issues with backslashes
image_path = r"C:\Users\abh04\OneDrive\Desktop\Project\Project\pencil sketch\dog.webp"

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Show the original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)

# Invert the grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey(0)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred = 255 - blurred

# Create pencil sketch using color dodge blend
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Show the final pencil sketch
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)

# Show both original and sketch again
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
