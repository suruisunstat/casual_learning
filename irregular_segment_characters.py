import cv2
os.chdir("/Users/suruisun/Downloads/")

img = cv2.imread('input.jpg')
result = img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
cv2.imwrite("thresh.jpg", thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
eroded = cv2.erode(thresh, kernel)
cv2.imwrite("eroded.jpg", eroded)

binary, contours, hierarchy = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

color = (0, 255, 0)
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
    temp = result[y:(y + h), x:(x + w)]
    cv2.imwrite("./result/" + str(x) + ".jpg", temp)

cv2.imwrite("result.jpg", img)
