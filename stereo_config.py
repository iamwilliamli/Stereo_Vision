import numpy as np
import cv2
from Stereo_Calibration import *
import os

#双目相机参数
class stereoCameral(object):
    def __init__(self):
        self.filepath = os.path.join(os.getcwd(),'Dataset/')
        self.cal_data = StereoCalibration(self.filepath, 0.215)
        #左相机内参数
        self.cam_matrix_left = self.cal_data.camera_model['M1']
        #右相机内参数
        self.cam_matrix_right = self.cal_data.camera_model['M2']

        #左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = self.cal_data.camera_model['dist1']
        self.distortion_r = self.cal_data.camera_model['dist2']

        #旋转矩阵
        om = self.cal_data.camera_model['R']
        self.R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
        #平移矩阵
        self.T = self.cal_data.camera_model['T']
