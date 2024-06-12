import cv2


source = '"File Location"'
destination = '"Destination"'
scale_width = 99
scale_height = 99

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_width = int(src.shape[1]* (scale_width/100))
new_height = int(src.shape[0]* (scale_height/100))

output = cv2.resize(src, (new_width, new_height))
a = cv2.imwrite(destination, output)
#To show image
# cv2.imshow("title", a)
# cv2.waitKey(0)