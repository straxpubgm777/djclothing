import torch
import torchvision
from torchvision import transforms as T
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
import json
import numpy as np
import os

ROOT_DIR = os.getcwd()

def train_clothes():
  annotation_file_path = f"{ROOT_DIR}/Dataset/annotation/train.json"
  with open(annotation_file_path, 'r') as f:
      annotations = json.load(f)

  img_path = f"{ROOT_DIR}/Dataset/images/habitat-habitat-damask-print-top_1.jpg"
  img = Image.open(img_path)

  regions = annotations.get("habitat-habitat-damask-print-top_1.jpg196393", {}).get("regions", [])

  body_mask = np.zeros_like(np.array(img))
  right_hand_mask = np.zeros_like(np.array(img))
  left_hand_mask = np.zeros_like(np.array(img))
  shorts_mask = np.zeros_like(np.array(img))
  pants_mask = np.zeros_like(np.array(img))


  for region in regions:
      shape_attributes = region.get("shape_attributes")
      region_attributes = region.get("region_attributes", {}).get("name", "")

      if shape_attributes:
          polygon = list(zip(shape_attributes.get("all_points_x", []), shape_attributes.get("all_points_y", [])))
          polygon = np.array(polygon, np.int32)
          polygon = polygon.reshape((-1, 1, 2))

          # Check the region attribute and draw on the corresponding mask
          if region_attributes == "body":
              cv2.fillPoly(body_mask, [polygon], color=(255, 255, 255))
          elif region_attributes == "right_hand":
              cv2.fillPoly(right_hand_mask, [polygon], color=(255, 255, 255))
          elif region_attributes == "left_hand":
              cv2.fillPoly(left_hand_mask, [polygon], color=(255, 255, 255))
          elif region_attributes == "shorts":
              cv2.fillPoly(shorts_mask, [polygon], color=(255, 255, 255))
          elif region_attributes == "pants":
              cv2.fillPoly(pants_mask, [polygon], color=(255, 255, 255))

  # Display the images only if the corresponding regions exist
  if np.any(body_mask):
      cv2.imwrite(f"{ROOT_DIR}/body_part.png",cv2.bitwise_and(np.array(img), body_mask))

  if np.any(right_hand_mask):
      cv2.imwrite(f"{ROOT_DIR}/right_hand.png",cv2.bitwise_and(np.array(img), right_hand_mask))

  if np.any(left_hand_mask):
      cv2.imwrite(f"{ROOT_DIR}/left_hand.png",cv2.bitwise_and(np.array(img), left_hand_mask))

  if np.any(shorts_mask):
      cv2.imwrite(f"{ROOT_DIR}/shorts.png",cv2.bitwise_and(np.array(img), shorts_mask))

  if np.any(pants_mask):
      cv2.imwrite(f"{ROOT_DIR}/pants.png",cv2.bitwise_and(np.array(img), pants_mask))