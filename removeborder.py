import cv2
import os
import numpy as np

input_folder = "input/"
output_folder = "output/"

# IT should be necessary to output folder exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# We have to loop through all files which are present in input folder 
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Image {filename} load nahi hui, skip kar rahe hain.")
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        height, width = edges.shape

        #Here is detect borders
        top = bottom = left = right = 0

        for i in range(height):
            if np.sum(edges[i, :]) > 0:
                top = i
                break

        for i in range(height - 1, -1, -1):
            if np.sum(edges[i, :]) > 0:
                bottom = height - i - 1
                break

        for j in range(width):
            if np.sum(edges[:, j]) > 0:
                left = j
                break

        for j in range(width - 1, -1, -1):
            if np.sum(edges[:, j]) > 0:
                right = width - j - 1
                break

        #  Here its Crop image
        cropped = image[top:height - bottom, left:width - right]

        #  We have to Save cropped image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, cropped)

        print(f"{filename} cropped and saved to output/")

print("\n All images processed!")
