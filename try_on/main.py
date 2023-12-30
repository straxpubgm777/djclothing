from rembg import remove
from PIL import Image
import cv2
import numpy as np
from poseEstimate import pose_estimate
from affine_transform import affine_transform
from train import train_clothes



clinet_path = Image.open("/content/clients_picture/1.jpg")

# Remove background
image_np = cv2.cvtColor(np.array(clinet_path), cv2.COLOR_RGB2BGR)
image_np = remove(image_np)
 
# check pose
image_np = cv2.cvtColor(np.array(image_np), cv2.COLOR_BGR2RGB)
client_pose = pose_estimate(image_np)
clothes_pose = train_clothes()

train_clothes()