from rembg import remove
from PIL import Image
import cv2
import numpy as np
from poseEstimate import pose_estimate
from affine_transform import affine_transform
from train import train_clothes
import os

ROOT_DIR = os.getcwd()

# put client's picture folder called "clients_picture" and write path of image
clinet_path = Image.open(f"{ROOT_DIR}/clients_picture/")

# Remove background
image_np = cv2.cvtColor(np.array(clinet_path), cv2.COLOR_RGB2BGR)
image_np = remove(image_np)
 
# check pose
image_np = cv2.cvtColor(np.array(image_np), cv2.COLOR_BGR2RGB)
client_pose = pose_estimate(image_np)
clothes_pose = train_clothes()

train_clothes()