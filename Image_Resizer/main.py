import cv2

# Configurable Parameters
source = "RR.jpg"
destination = "RR3.jpeg"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("Rolls Royce", src) --> To run this cv2.waitKey (at last ) is needed, so first uncomment it if you want to run it.

# Percent by which the image is resized

# Calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)