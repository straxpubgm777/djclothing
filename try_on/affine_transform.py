import os 
import cv2
import numpy as np
import matplotlib as plt
from google.colab.patches import cv2_imshow

def affine_transform(clothes,person):
  ROOT_DIR = os.getcwd()
  img = cv2.imread(f"{ROOT_DIR}/right_hand.png")
  img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

  height,width,_ = img.shape

  p1 = np.array([[100,100],
                 [900,100],
                 [100,900]], dtype=np.float32)
  
  p2 = np.array([[50,150],
                 [900,100],
                 [150,800]], dtype=np.float32)
  T = cv2.getAffineTransform(p1,p2)
  imgTrans = cv2.warpAffine(img,T,(width,height))

  cv2.imwrite("qwe.png",imgTrans)