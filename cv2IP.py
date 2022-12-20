import cv2
import numpy as np
import enum 

class BaseIP:
    def __init__(self):
        pass

    #將picture做成多為陣列並回傳
    @staticmethod
    def ImRead(picture):
        return cv2.imread(picture)

    #將filename放入保存image的資料目錄中
    @staticmethod
    def ImWrite(picture,image):
        cv2.imshow(picture,image)
    
    #陣列轉換成圖
    @staticmethod
    def ImShow(window_name, picture):
        cv2.imshow(window_name,picture)

    #建立視窗
    @staticmethod
    def ImWindow(window_name, flags):
        cv2.namedWindow(window_name, flags)

#AlphaIP繼承BaseIP
class AlphaIP(BaseIP):
    def __init__(self):
        pass

    #將picture做成多為陣列並回傳，-1是開通第四維度
    @staticmethod
    def ImRead(picture):
        return cv2.imread(picture,-1)

    #此函數用來分離前景影像的RGB影像資訊及Alpha通道資訊
    @staticmethod
    def SplitAlpha(SrcImg):
        b,g,r,a = cv2.split(SrcImg)
        foreground = cv2.merge((b,g,r))
        alpha = cv2.merge((a,a,a))
        return [foreground,alpha]

    #此函數用來使用Alpha通道來混合前景與背景影像
    @staticmethod
    def DoBlending(Foreground, Background, Alpha):
        foreground = cv2.multiply(Alpha, Foreground)
        background = cv2.multiply(1.0 - Alpha, Background)
        outImage = cv2.add(foreground, background)
        return outImage


