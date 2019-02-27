import numpy as np 
import matplotlib.pyplot as plt 


def poly_info(x,y,order_number):
    z = np.polyfit(x,y,order_number)
    p = np.poly1d(z)
    xp = np.linspace(0,20,1)
    

    

    
    #_= plt.plot(x,y,'.',xp,p(xp),'-')
    
    ''' 
    plt.xlim(0,20)
    plt.ylim(0,1)
    plt.grid(True)

    plt.show()
    print(p)
    '''
    return z[0] , z[1] , z[2]


