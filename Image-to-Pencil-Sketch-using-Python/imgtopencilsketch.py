import cv2
import matplotlib.pyplot as plt
from IPython import display

# pip install matplotlib

# 2023-05-26 ngio add
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

img=cv2.imread('dog.jpg',0)
display.Image("dog.jpg",width=250)



#Color value just for own sake
print('Minimum color range',img.min())
print('Maximum color range',img.max())


#Converting image to greyscale
#plt.imshow(img,cmap='gray')
#plt.title('Black and white imege')
#plt.show()

#Inverting the image
inv=255-img
#plt.title('Inverted imege')
#plt.imshow(inv,cmap='gray')
#plt.show()

##Applying Gaussian blur to smooth out the image
gblur=cv2.GaussianBlur(inv,ksize=(21,21),sigmaX=0,sigmaY=0)
#plt.title('Imege after Gaussian blur applied')
#plt.imshow(gblur,cmap='gray')
#plt.show()

##Color Dodging and burning (Final pencil sketch output)
dodge= lambda image,mask: cv2.divide(image,255-mask,scale=256)
blended=dodge(img,gblur)
plt.title('Pencil sketch of image')
plt.imshow(blended,cmap='gray')

# Save the image as a PNG file
plt.savefig("dog_sketch.png", dpi=200)

plt.show()



