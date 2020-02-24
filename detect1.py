import cv2

image = cv2.imread("C:\\sample.jpg") 
img = cv2.resize(myImage,(640,480))        
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1,10, param1=50,param2=35,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(myImage,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(myImage,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',myImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
