import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import polyfit
from tqdm import tqdm
import matplotlib as mpl
import scipy.stats
#------------------------------------------------------------------------------
##############find The Correlation coefficient################
#1 = 760:860,1125:1225 กลาง  140:240,350:450            บริเวณ 1      180:280,500:600 
 #2 = 740:840,950:1050   ต้นฝัก 160:260,140:240                        180:280,400:500
#3 = 780:880,1400:1500  ปลายฝัก  140:240,600:700                      180:280,700:800                                   
#470:520,1200:1250   , 510:560,1010:1070  , 520:570,1180:1230
#260:310,1000:1050 , 370:420,1020:1070,350:400,1080:1130

for num in (range(29,30,1)):

    img1 =cv2.imread('test7/data'+str(num) +"/0.jpg")
    

    img1 = img1[180:280,500:600 ]    ### 100*100




    mean1 = np.mean(img1)

    height = np.size(img1, 0)
    width = np.size(img1, 1)

    k = 1             ## select window 

    h1 = 0
    h2 = height
    w1 = 0
    w2 = width



    UPPER1 = []  ##
    LOWER1 = []  ##  list
    LOWER2 = []  ##


    SUM1 = 0
    SUM2 = 0
    SUM3 = 0


    for pic in (range(0,200,1)):
        M ='test7/data'+str(num)+"/" +str(pic)+ ".jpg"
        
        

        img2 = cv2.imread(M)
        img2 = img2[180:280,500:600  ]
        mean2 = np.mean(img2)

        UPPER1.append(SUM1)
        LOWER1.append(SUM2)
        LOWER2.append(SUM3)

        SUM1 = 0
        SUM2 = 0
        SUM3 = 0



        for row in range(h1, h2,1):
                for col in range(w1, w2,1):
                    
                    y = (k*row)
                    x = (k*col)
                    
                    px1 = img1[y,x]  
                    px2 = img2[y,x]  

                    
                    D1 = px1-mean1    
                    D2 = px2-mean2   
            

                    D3 = D1*D2            ######  UPPER1
                    S1 = np.square(D1)    ######  LOWER1
                    S2 = np.square(D2)    ######  LOWER2

                                        
                    SUM1 +=  D3
                    SUM2 +=  S1
                    SUM3 +=  S2
        # print('Processing... %.2f'%(pic*100/200))
    
    del UPPER1[0]
    del LOWER1[0]
    del LOWER2[0]  




    r = []    #### list
    corr2 = 0
    u = len(UPPER1)
    p = np.zeros(200)
    p = []

    for c in range(0,u,1):

        r.append(corr2)
        corr2 = 0
        
        corr2 = UPPER1[c]/np.sqrt(LOWER1[c]*LOWER2[c])  
        
        p.append(corr2[0])
        #p.append(corr2[1])
        #p.append(corr2[2])
    del r[0]

    #print('p=',p)


    t = np.arange(0.01,len(p)/10,0.1)


    w = len(p)
    #print(w)

    q = np.arange(w)

    fp = mpl.font_manager.FontProperties(family='RSU',size=16)
    


    ax = plt.gca()
   
    ax.plot(t,p,'b.-') 
    

    plt.ylabel('Correlation coefficient')
    plt.xlim(0,20)
    plt.ylim(0,1)
    plt.xlabel('Time(S)')

    plt.grid(True)

    plt.savefig('test7/save1/'+str(num)+".jpg")

    plt.cla()   # Clear axis
    plt.clf()   # Clear figure
    plt.close() 


    a ,b,c = polyfit.poly_info(t,p,2)

    x = 5
    y = (a*x*x) + (b*x) + c

    #print( a, b,c)
    print(y)