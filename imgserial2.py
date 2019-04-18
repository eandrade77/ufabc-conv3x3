
import cv2
import matplotlib.pyplot as plt
import numpy as np
from bitstream import BitStream
from numpy import int8

im = cv2.imread('test.png',0)
#im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
#plt.imshow(im)

#print (im)

print (im.shape)

y, x = im.shape

print(y, x)

#print(format(5, "b"))

#print(im[70:71])

imout=im

stream = BitStream()

stream_in = BitStream()


#bit={0,0,0,0,0,0,0,0}

# cv2.imwrite('testgray.png',im)
# for j in range(x):
# 	print(j)
# 	for i in range(y):
# 		#print(i)
# 		value=im[i,j]
# 		#bit = format(value,"b").zfill(8)
# 		stream.write(value, int8)
		
# 		bit=str(stream.read(BitStream,8))
			
# 		#print(bit)
# 		datab=(bit[0], bit[1], bit[2], bit[3], bit[4], bit[5], bit[6], bit[7])
# 		datain=int(''.join(datab),2)
# 		#datain="00000111"
# 		imout[i,j]=datain*2
		#print(value, datab, datain)
#bit = format(15,"b").zfill(8)

bit=[8]

def calcs(image, y, x):
	start_time = time.time()
	#image=image
	for j in range(x):
	 	#print(j)
	 	for i in range(y):
	 		value=image[i,j]
	 		stream.write(value, int8)
	 		#bit=[stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1),stream.read(BitStream,1)]
	 		#databb=(bit[0], bit[1], bit[2], bit[3], bit[4], bit[5], bit[6], bit[7])
	 		#datainb=int(''.join(databb),2)
	 		#datain="00000111"
	 		#image[i,j]=datainb
	 		#image[i,j]=value
	print(len(stream))

	for k in range(len(stream)):
		print(stream.read(BitStream,1))


	print("FPS: ", 1.0 / (time.time() - start_time))
	return image

#data=(bit[0], bit[1], bit[2], bit[3], bit[3], bit[4], bit[5], bit[6], bit[7])


#a = [1, 2, 3, 4, 5]

#b=np.pad(a, (1, 1), 'constant', constant_values=(0,0))

#print(b)

#print(im[70,120])

#print(format(im[70,120],"b"))


cv2.imwrite('testgray_out.png',imout)

#plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))

#plt.show()

import cv2
 
captura = cv2.VideoCapture(0)

import time

#while True:
    #start_time = time.time() # start time of the loop

    ########################
    # your fancy code here #
    ########################

    #print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop


while(1):
    #start_time = time.time() # start time of the loop
    ret, frame = captura.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    y, x = gray.shape
    cv2.imshow("Video", calcs(gray, y, x))
	#print(gray)
	#print("FPS: ", 1.0 / (time.time() - start_time))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
captura.release()
cv2.destroyAllWindows()




def calcso(image, y, x):
	start_time = time.time()
	image=image
	for j in range(x):
	 	#print(j)
	 	for i in range(y):
	 		#print(i)
	 		value=image[i,j]
	 		bit = format(value,"b").zfill(8)
	 		#print(bit)
	 		databb=(bit[0], bit[1], bit[2], bit[3], bit[4], bit[5], bit[6], bit[7])
	 		datainb=int(''.join(databb),2)
	 	#datain="00000111"
	 		image[i,j]=datainb/4
	 		#image[i,j]=value
	print("FPS: ", 1.0 / (time.time() - start_time))
	return image