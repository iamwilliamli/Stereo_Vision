import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt
import time

filepath = '/home/william/Documents/Stereo_Camera_Measurement/Dataset/'
file_num = 1

# for file_name in (glob.glob(filepath + 'right_obj/*.jpeg')):
#     file_num = file_name.split('/')[-1].split('.')[0]
#     imgR = cv2.imread(filepath + 'right_obj/'+str(file_num) + '.jpeg', 0)
#     imgL = cv2.imread(filepath + 'left_obj/'+str(file_num) + '.jpeg', 0)
#     win_size = 5
#     min_disp = -1
#     max_disp = 63 #min_disp * 9
#     num_disp = max_disp - min_disp # Needs to be divisible by 16
#     #Create Block matching object. 
#     stereo = cv2.StereoSGBM_create(minDisparity= min_disp,
#     numDisparities = num_disp,
#     blockSize = 5,
#     uniquenessRatio = 5,
#     speckleWindowSize = 5,
#     speckleRange = 5,
#     disp12MaxDiff = 1,
#     P1 = 8*3*win_size**2,#8*3*win_size**2,
#     P2 =32*3*win_size**2) #32*3*win_size**2)
#     #Compute disparity map
#     print ("\nComputing the disparity  map...")
#     disparity_map = stereo.compute(imgR, imgL)

#     #Show disparity map before generating 3D cloud to verify that point cloud will be usable. 
#     plt.imshow(disparity_map,'gray')
#     plt.show()
#     plt.close('all')

import scipy.signal as signal

filepath = os.path.join(os.getcwd(),'Dataset/')

# for file_name in (glob.glob(filepath + 'right/*.jpeg')):
#     file_num = file_name.split('/')[-1].split(' ')[-1].split('.')[0]
#     imgR = cv2.imread("/home/william/Documents/Stereo_Camera_Measurement/Dataset/right.png", 0)
#     imgL = cv2.imread("/home/william/Documents/Stereo_Camera_Measurement/Dataset/left.png", 0)
#     imgR = imgR[0:482,0:360]
#     imgL = imgL[0:482,0:360]
#     # imgR = cv2.imread(filepath + 'right/cam_2 '+str(file_num) + '.jpeg', 0)
#     # imgL = cv2.imread(filepath + 'left/cam_1 '+str(file_num) + '.jpeg', 0)
#     stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
#     disparity = stereo.compute(imgL,imgR)
#     plt.imshow(disparity,'gray')
#     plt.show()
imgR = cv2.imread(filepath + 'right/'+str(file_num) + '.jpeg', 0)
imgL = cv2.imread(filepath + 'left/'+str(file_num) + '.jpeg', 0)
win_size = 5
min_disp = -1
max_disp = 63 #min_disp * 9
num_disp = max_disp - min_disp # Needs to be divisible by 16
#Create Block matching object. 
stereo = cv2.StereoSGBM_create(minDisparity= min_disp,
 numDisparities = num_disp,
 blockSize = 5,
 uniquenessRatio = 5,
 speckleWindowSize = 5,
 speckleRange = 5,
 disp12MaxDiff = 1,
 P1 = 8*3*win_size**2,#8*3*win_size**2,
 P2 =32*3*win_size**2) #32*3*win_size**2)
#Compute disparity map
print ("\nComputing the disparity  map...")
disparity_map = stereo.compute(imgR, imgL)
disparity_map = signal.medfilt(disparity_map,(3,3)) # Median Filtering
#Show disparity map before generating 3D cloud to verify that point cloud will be usable. 
plt.figure()
plt.imshow(imgL)
plt.figure()
plt.imshow(disparity_map,'gray')
kernel = np.ones((2,2),np.uint8)  
erosion = cv2.erode(disparity_map,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
plt.figure()
plt.imshow(erosion,'gray')
plt.show()
plt.close('all')

