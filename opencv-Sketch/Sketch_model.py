import cv2

class Sketch:
    def __init__(self, imgpath, savepath, savename):
        self.imgpath = imgpath
        self.savepath = savepath
        self.savename = savename

    def sketchit(self):
        image  = cv2.imread(self.imgpath)
        image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image_gray_neg = 255-image_gray
        image_blur = cv2.GaussianBlur(image_gray_neg,(25,25),sigmaX=0,sigmaY=0)
        final_sketch = self.dodge(image_gray,image_blur)
        cv2.imwrite(self.savepath +"/"+ self.savename,final_sketch)

    def dodge(self,image,mask):
        return cv2.divide(image, 255 - mask, scale=256)

    def burn(self,image,mask):
        return 255 - cv2.divide(255 - image, 255 - mask, scale=256)
