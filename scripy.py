import cv2

# Read the image
img = cv2.imread("C:/Users/naina/Downloads/Pyhton programs of PRO! classes/PRO-104-Project-Image-main/solar-system.jpg")  # Replace with the path to your image

# Define font and text properties
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.5
color = (255, 255, 255)  # White color in BGR format

# Add labels for Sun, Mercury, Venus, and Earth with their corresponding coordinates
cv2.putText(img, "Sun", (20, 300), font, font_scale, color)
cv2.putText(img, "Mercury", (110, 180), font, font_scale, color)
cv2.putText(img, "Venus", (190, 270), font, font_scale, color)
cv2.putText(img, "Earth", (300, 270), font, font_scale, color)
cv2.putText(img, "Mars", (410, 270), font, font_scale, color)
cv2.putText(img, "Jupiter", (500, 810), font, font_scale, color)
cv2.putText(img, "Saturn", (600, 600), font, font_scale, color)
cv2.putText(img, "Uranus", (690, 510), font, font_scale, color)
cv2.putText(img, "Neptune", (800, 500), font, font_scale, color)

# Display the image with labels
cv2.imshow("Image with labels", img)
cv2.waitKey(0)  # Wait for a keypress to close the window
cv2.destroyAllWindows()
