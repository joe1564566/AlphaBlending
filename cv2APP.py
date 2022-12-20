import cv2IP
import cv2
import numpy as np

def base():
    ip = cv2IP.BaseIP()
    img = ip.ImRead("dra.jpg")
    img = np.full((240,320), 100, np.uint8)
    cv2.waitKey(0)

def blend(Fore_img, Back_img):
    ip = cv2IP.AlphaIP()
    img = ip.ImRead(Fore_img)
    fore_alpha = ip.SplitAlpha(img)  #得到前景与alpha通道                        
    fore = np.float32(fore_alpha[0]) #前景BGR 
    alpha = np.float32(fore_alpha[1])/255 #alpha通道
    ImDim = alpha.shape #獲取alpah通道的圖片大小
    back = ip.ImRead(Back_img) #讀取背景
    if (ImDim[0] != back.shape[0]) or (ImDim[1] != back.shape[1]):
        back = cv2.resize(back,(ImDim[1], ImDim[0])) #使背景與前景大小相同
    
    back = np.float32(back) #轉換為32位元
    out = ip.DoBlending(fore, back, alpha) #結合
    out = np.uint8(out) #輸出8位元的影像
    back = np.uint8(back)
    ip.ImShow("back",back)
    ip.ImShow("Out",out)
    ip.ImShow("alpha", alpha)
    cv2.waitKey(0)

if __name__ == "__main__":
    #base()
    blend("Doge.png","backgrand.png")