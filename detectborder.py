import cv2
import os

# Step 1:  We have to Load image
image_path = "input/IMG_1.jpg"   # Update with your actual file name
image = cv2.imread(image_path)
if image is None:
    print("Image load nahi hui — path galat hai ya image corrupt hai.")
    exit()
    print("Original Image Shape:", image.shape)



# Step 2: We have to Convert it in  grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_sample.jpg", gray)
print("Grayscale image saved as gray_sample.jpg")




# Step 3:  In this steps Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)  



# Step 4: Here is to  Save edge-detected image
cv2.imwrite("edges_sample.jpg", edges)




import numpy as np

# Step: Image dimensions
height, width = edges.shape

# Step: Border thickness initiliazing
topborder = 0
bottomborder = 0
leftborder = 0
rightborder = 0

#  Top border detecting
for i in range(height):
    if np.sum(edges[i, :]) > 0:  # row has white pixels
        topborder = i
        break

#  Bottom border Detecting
for i in range(height-1, -1, -1):
    if np.sum(edges[i, :]) > 0:
        bottomborder = height - i - 1
        break

#  Left border Detect
for j in range(width):
    if np.sum(edges[:, j]) > 0:  # column has white pixels
        leftborder = j
        break

#  Right border Detecting
for j in range(width-1, -1, -1):
    if np.sum(edges[:, j]) > 0:
        rightborder = width - j - 1
        break

# Step:  Detected borders Printing
print("\nDetected Border Thickness (in pixels):")
print(f"Top: {topborder}")
print(f"Bottom: {bottomborder}")
print(f"Left: {leftborder}")
print(f"Right: {rightborder}")




import csv

# Step: In this steps We Write CSV file
csv_filename = "result.csv"

# Agar file already exist hai, to overwrite karega
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["image_name", "top_border", "bottom_border", "left_border", "right_border"])
    writer.writerow([os.path.basename(image_path), topborder, bottomborder, leftborder, rightborder])

print(f"\nBorder details saved in {csv_filename}")


