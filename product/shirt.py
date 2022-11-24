import cv2
import numpy as np
from PIL import Image

# 
def get_result_shirt(user_image):
    Backgrund= cv2.imread("base_image/shirt.png")
    overlay = cv2.imread("C:\Users\BeomKi\Desktop\asdasfsgd\Uhwa_Backend\base_image"+user_image)
    
# ------------------------------------- overlay model 적용 시작 ---------------------------------------------------------------
    net = cv2.dnn.readNetFromTorch('models/instance_norm/starry_night.t7')
    # 모델을 바꾸고싶으면 경로변경
    # 위 세가지는 유저가 변경가능
    # 11~24번쨰줄까지는 수정하지마세요
    MEAN_VALUE = [103.939, 116.779, 123.680]
    #이 모델의 가장성능이 좋은 값
    blob = cv2.dnn.blobFromImage(overlay, mean=MEAN_VALUE)
    #전처리 하는데 차원변형
    net.setInput(blob)
    overlay = net.forward()
    overlay = overlay.squeeze().transpose((1, 2, 0))
    # 사람이 이해하기쉽게 후처리 시작

    overlay += MEAN_VALUE
    overlay = np.clip(overlay, 0, 255)
    overlay = overlay.astype('uint8')
    # 컴퓨터의언어에서 다시 사람의언어로 읽기쉽게 변형
    # # -------------------------------------overlay model 적용 끝 ---------------------------------------------------------------
    # -------------------------------------업로드 이미지(.png) 배경 지우기  시작 ---------------------------------------------------------------
    overlay = cv2.resize(overlay, dsize=(400,450))
    h, w ,c = overlay.shape

    shapes = np.zeros_like(Backgrund, np.uint8)

    shapes[0+200:h+200, 300+0:w+300] = overlay
    # cv2.imshow('shapes.png', shapes)
    # cv2.imshow('overlay.png', overlay)
    alpha = 0.5
    mask = shapes.astype(bool)
    # -------------------------------------업로드 이미지(.png) 배경 지우기 끝---------------------------------------------------------------
    # -------------------------------------이미지 색상 변경 시작 ---------------------------------------------------------------

    # -------------------------------------이미지 색상 변경 끝 ---------------------------------------------------------------
    # Backgrund[mask] = shapes[mask]
    Backgrund[mask] = cv2.addWeighted(shapes, alpha, shapes, 1 - alpha, 0)[mask]


















# # ------------------------------------- overlay model 적용 시작 ---------------------------------------------------------------
# net = cv2.dnn.readNetFromTorch('models/instance_norm/mosaic.t7')
# MEAN_VALUE = [103.939, 116.779, 123.680]
# #이 모델의 가장성능이 좋은 값
# blob = cv2.dnn.blobFromImage(overlay, mean=MEAN_VALUE)
# #전처리 하는데 차원변형
# net.setInput(blob)
# overlay = net.forward()
# overlay = overlay.squeeze().transpose((1, 2, 0))
# # 사람이 이해하기쉽게 후처리 시작

# overlay += MEAN_VALUE
# overlay = np.clip(overlay, 0, 255)
# overlay = overlay.astype('uint8')
# # 컴퓨터의언어에서 다시 사람의언어로 읽기쉽게 변형
# # -------------------------------------overlay model 적용 끝 ---------------------------------------------------------------