import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#700:850,1050:1200

pic = cv2.imread('test7/data3/100.jpg')
#pci = cv2.medianBlur(pic,7)
plt.imshow(pic)
plt.show()

#print(pic.shape)
#crop = pic[0:,0:]
crop = pic[100:250,350:500]
plt.imshow(crop)
plt.show()

cv2.imwrite('test7/p.jpg',crop)

i1 = cv2.imread('test7/p.jpg')
i2 = cv2.imread('test7/p.jpg')

height = np.size(i1,0)
width = np.size(i2,1)



k = 5
h1 = int((height/k)/49)
h2 = int((height/k)+1)
w1 = int((width/k)/49)
w2 = int((width/k)+1)


for row in range(h1, h2):    # number of row / window 
    for col in range(w1, w2): # number of col / window
        y1 = (k*row)-k
        y2 = (k*row)
        x1 = (k*col)-k
        x2 = (k*col)
        
        roi = i2[y1:y2, x1:x2]  #select a region of image
             
        SD = np.std(roi)      # find standard deviation of region
        print(SD)
        mean = np.mean(roi)   # find mean of region

        Contrast = SD/mean    # find Contrast

        gray = Contrast*255   # Contrast to gray scale

        i2[y1:y2, x1:x2] = [gray] # modifies image

r =[]
#edian =  cv2.bilateralFilter(i2,9,75,75)

plt.imshow(i2)
plt.show()
cv2.imwrite("test7/LA.jpeg", i2)

x = cv2.imread("test7/LA.jpeg")
x= cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)

r.append(x[0])

print(len(r[0]))


'''


plt.plot(r[0]) 



plt.grid(True)
plt.show()


'''



'''
y = cv2.addWeighted(x,2,np.zeros(x.shape,x.dtype),70,1)
x1 = cv2.addWeighted(x,2,np.zeros(x.shape,x.dtype),70,1)

#blur = cv2.bilateralFilter(x1,9,75,0)


blur = cv2.medianBlur(x1,5)

plt.figure(figsize=(12,5))
plt.subplot(1,3,1);
plt.imshow(pic)

plt.subplot(1,3,2);
plt.imshow(i2)

plt.subplot(1,3,3);
plt.imshow(blur)


plt.show()
'''
#cv2.imwrite('test6/LA.jpeg',i2)




'''






k = 5





h1 = 0
h2 = height
w1 = 0
w2 = width



for row in range (h1,h2):
	for col in range (w1,w2):
		
		y1 = row
		y2 = row+k
		x1 = col
		x2 = col+k
		
		roi = i1[y1:y2,x1:x2]
		SD = np.std(roi)
		mean = np.mean(roi)
		Contrast = SD/mean
		gray = Contrast*255
		i2[y1:y2,x1:x2]=[gray]

gamma = 0.9
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
res = cv2.LUT(i2, lookUpTable)	

plt.imshow(res)
plt.show()
'''

'''    
cv2.imwrite('LA.jpeg',i2)

print('finish')
'''
