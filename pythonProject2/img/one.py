import cv2
import numpy as ny

img = cv2.imread('IMG-20230719-WA0013.jpg')

row1=60
row2=172
afteritrationtobeaddinrow = 112
column=36
column2=314
count = 1
imagenamecounter = 1
for i in range(int(1280/112+60)):
    if(count > 5):
        break
    for j in range(int(904/278+36)):
        crop = img[row1:row2, column:column2]
        cv2.imwrite('C:/Users/harsh.bhawsar_infobe/PycharmProjects/pythonProject2/img/temp/'+str(imagenamecounter)+'.jpg', crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        column = column2
        column2 += 278
        imagenamecounter+1
    row1 = row2
    row2 += 112
    count+1

img1 = cv2.imread('top1.jpg')
img2 = cv2.imread('22.jpg')
im_v = cv2.vconcat([img1, img2])
cv2.imwrite('C:/Users/harsh.bhawsar_infobe/PycharmProjects/pythonProject2/img/result/new.jpg',im_v)
