import cv2
import numpy as np

# Load the image
img = cv2.imread('../IMG-20230719-WA0013.jpg')
print(img.shape)

# Define initial values for rows and columns
row1 = 60
row2 = 172
after_iteration_to_be_added_in_row = 112
column = 36
column2 = 314
count = 1
imagenamecounter = 1

# Loop to crop the image
for i in range(int(1280 / 112)):
    if count > 5:
        break

    for j in range(int(904 / 278)):
        crop = img[row1:row2, column:column2]
        cv2.imwrite('C:/Users/harsh.bhawsar_infobe/PycharmProjects/pythonProject2/img/temp/' + str(imagenamecounter) + '.jpg', crop)
        column = column2-2
        column2 += 278
        imagenamecounter += 1  # Corrected this line, you need to use '+=' to increment the counter

    row1 = row2
    row2 += after_iteration_to_be_added_in_row  # Corrected the variable name here
    column = 36
    column2 = 314
    count += 1  # Corrected this line, you need to use '+=' to increment the count
