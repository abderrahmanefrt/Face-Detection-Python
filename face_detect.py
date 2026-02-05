import cv2 as cv

img=cv.imread('group 1.jpg')
cv.imshow('Original image', img)

gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray)

haar_cascade =cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
print(f'Number of faces found ={len(faces_rect)}')

for(x, y, w, h) in faces_rect:
  cv.rectangle(img ,(x,y),(x+w, y+h), (0,255,0),2)


cv.imshow('Detected faces', img)
cv.waitKey(0)