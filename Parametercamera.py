import RPi.GPIO as GPIO

import PySpin
import cv2
import time


NUM_IMAGES = 1


analys_SW = 5
            
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(analys_SW ,GPIO.IN)



#------------------------------------------------------------------------------setting camera--------------------------------------------------------------------------------------------------------------------------------------------
def configure_custom_image_settings(cam):  

    result =1
    
    
    cam.PixelFormat.SetValue(PySpin.PixelFormat_Mono8)
    node_offset_x =554 #PySpin.CIntegerPtr(nodemap.GetNode('OffsetX'))
    if PySpin.IsAvailable(node_offset_x) and PySpin.IsWritable(node_offset_x):

            node_offset_x.SetValue(0)
            print 'Offset X set to %i...' % node_offset_x.GetMin()
            
    else:
            print 'Offset X not available...'

        # Apply minimum to offset Y
        #
        # *** NOTES ***
        # It is often desirable to check the increment as well. The increment
        # is a number of which a desired value must be a multiple of. Certain
        # nodes, such as those corresponding to offsets X and Y, have an
        # increment of 1, which basically means that any value within range
        # is appropriate. The increment is retrieved with the method GetInc().
    node_offset_y = 392#PySpin.CIntegerPtr(nodemap.GetNode('OffsetY'))
    if PySpin.IsAvailable(node_offset_y) and PySpin.IsWritable(node_offset_y):

            node_offset_y.SetValue(0)
            print 'Offset Y set to %i...' % node_offset_y.GetMin()

    else:
            print 'Offset Y not available...'



    
    
    cam.Width.SetValue(400)
    cam.Height.SetValue(400)
 

 	
         

 
    return result

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def print_device_info(cam):

    result = True
    

    return result

#------------------------------------------------------------------------------Save Picture--------------------------------------------------------------------------------------------------------------------------------
def acquire_images(cam):



   
    result = True
    cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)
    cam.BeginAcquisition()
    

    
    #for i in range(1000):
    while(1):   
                            
                            image_result = cam.GetNextImage()
                            image_data =  image_result.GetNDArray()


                            print(image_data.shape)

                            
                          

                            image_converted = image_result.Convert(PySpin.PixelFormat_Mono8)
                            
                            filename = 'SCR/Raw_Pic.jpg' 
                            image_converted.Save(filename)
                            
                            
                            x = cv2.imread('SCR/Raw_Pic.jpg')
                            #cv2.startWindowThread()
                            cv2.namedWindow("Camera")
                            cv2.imshow('Camera',x)
                            
                            status = GPIO.input(analys_SW)
                            if  cv2.waitKey(1) & 0xFF == 27  or status == 0:
                                        cv2.destroyAllWindows()
                                        break
                                        
                                        
                                
                                

                            
                            print 'Image saved %d '
                            
                               
                            
                            
                           
  
    
   
    #cv2.destroyAllWindows()                       
    image_result.Release()
    cam.EndAcquisition()
    
    return result
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def run_single_camera(cam):

  
        
    try:
        # Initialize camera
        cam.Init()

        # Print device info
        result = print_device_info(cam)

        # Configure exposure
        if not configure_custom_image_settings(cam):
            return False

        # Acquire images
        result &= acquire_images(cam)
     
        # Deinitialize camera
        cam.DeInit()

        return result

    except PySpin.SpinnakerException as ex:
        print 'Error: %s' % ex
        return False

    
#--------------------------------------------------------------------------------Main Function---------------------------------------------------------------------------------------------------------------------------------
def getSingleImage():

    result = True
    NUM_IMAGES = 1
    
    system = PySpin.System.GetInstance()
    version = system.GetLibraryVersion()
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize()

   

   

    
    for i, cam in enumerate(cam_list):
        result &= run_single_camera(cam)
       
        
    del cam

    
    cam_list.Clear()
    system.ReleaseInstance()
    
    


 
#--------------------------------------------------------------------------------Main Function---------------------------------------------------------------------------------------------------------------------------------




