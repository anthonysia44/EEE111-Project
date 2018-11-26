#importing necessary packages 
from lights import Neon_Filter
import face_recognition
import numpy as np
import cv2

#Reads the filter from the same location/folder the code is run from
neon = cv2.imread("filter.png", -1) 
cap = cv2.VideoCapture(0) 

while True:
	lights = Neon_Filter()
	ret, image = cap.read()
	img_frame = image[:, :, ::-1]
	#this variable will find the face locations in the webcam
	ext = face_recognition.face_locations(img_frame)
	faces = [(0,0,0,0)] #initializes the coordinates of the face
	#if there is a face detected, then this part will be executed
	if ext != []:
		faces = [[ext[0][3], ext[0][0], abs(ext[0][3] - ext[0][1]) + 150, abs(ext[0][0] - ext[0][2])]]
		for (x, y, w, h) in faces:
			#Manually adjust the location of image filter within the face detected
			x -= 60
			w -= 30
			y -= 35
			h -= 10			
			neon_min = int(y - 3 * h / 5)
			neon_max = int(y + 8 * h / 5)
			face_neon = neon_max - neon_min
			face_frame = image[neon_min:neon_max, x:x+w]
			neon_resized = cv2.resize(neon, (w, face_neon), interpolation=cv2.INTER_CUBIC) #resizing the filter  
			lights.overlay(face_frame, neon_resized) #calls the overlay method from the Mask class

	#shows video stream with the title
	cv2.imshow("Neon Filter", image)

	#press esc to quit
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()
	
