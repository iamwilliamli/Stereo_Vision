import cv2
import numpy as np
import os 
import numpy as np

def disparity(x_r, y_r, x_l, y_l):
    return x_l - x_r


def on_EVENT_LBUTTONDOWN_r(event, x, y, flags, param):
    global rcounter, lcounter, x_l, y_l, x_r, y_r 
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(r_img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(r_img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255,25,25), thickness = 1)
        cv2.imshow("right camera image", r_img)
        print("r x: ",x,"y: ",y)
        rcounter = rcounter + 1
        x_r = x; y_r = y
        if rcounter == lcounter:
            print('disparity of this point: ', disparity(x_r, y_r, x_l, y_l))   
    return x, y

def on_EVENT_LBUTTONDOWN_l(event, x, y, flags, param):
    global rcounter, lcounter, x_l, y_l, x_r, y_r 
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(l_img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(l_img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255,25,25), thickness = 1)
        cv2.imshow("left camera image", l_img)
        print("l x: ",x,"y: ",y)
        lcounter = lcounter + 1
        x_l = x; y_l = y
        if rcounter == lcounter:
            print('disparity of this point: ',disparity(x_r, y_r, x_l, y_l)) 
    return x, y


if __name__ == "__main__":
    
    filepath = os.path.join('Dataset', 'object')
    left_obj  = os.path.join(filepath , "left_obj","1.jpeg")
    right_obj = os.path.join(filepath , "right_obj","1.jpeg")
    r_img = cv2.imread(right_obj)
    l_img = cv2.imread(left_obj)

    lcounter = 0
    rcounter = 0

    x_l = 0
    y_l = 0

    x_r = 0
    y_r = 0

    cv2.namedWindow("right camera image")
    cv2.setMouseCallback("right camera image", on_EVENT_LBUTTONDOWN_r)
    cv2.namedWindow("left camera image")
    cv2.setMouseCallback("left camera image", on_EVENT_LBUTTONDOWN_l)

    while(1):
        cv2.imshow("right camera image", r_img)
        cv2.imshow("left camera image", l_img)
        #file.write(x,y)# x,y是你获取到的坐标值
        if cv2.waitKey(0)&0xFF==27:
            break
    cv2.destroyAllWindows()
