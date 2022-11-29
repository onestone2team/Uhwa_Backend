import cv2
import os
import numpy as np
from PIL import Image
# print(os.path.abspath("starry_night.t7"))
def model(userimage,model):

    # "C:/Users/BeomKi/Desktop/asdasfsgd/Uhwa_Backend"+
    model_list=["candy","feathers","mosaic","la_muse","starry_night","the_scream","udnie"]
    overlay = cv2.imread(userimage[1:])
    # C:\Users\BeomKi\Desktop\asdasfsgd\Uhwa_Backend\11
    # /media/22/11/di2_ZO9NFbc.jpeg
    if model in model_list:
# ------------------------------------- overlay model 적용 시작 ---------------------------------------------------------------
    # "candy""feathers""mosaic""la_muse""starry_night""the_scream""udnie"
        net = cv2.dnn.readNetFromTorch('product/models/instance_norm/'+model+'.t7')
        # C:/Users/BeomKi/Desktop/asdasfsgd/Uhwa_Backend/starry_night.t7
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
        cv2.imwrite(userimage[1:],overlay)
        return userimage
    else:
        cv2.imwrite(userimage[1:],overlay)
        return  userimage


def get_result_shirt(img_read,category):
    if category ==1:
        category ="shirt"
    elif category ==2:
        category ="cap"
    elif category ==3:
        category="Hood"
    Backgrund= cv2.imread("product/base_image/"+category+".png")
    overlay=cv2.imread(img_read[1:])
    # -------------------------------------업로드 이미지(.png) 배경 지우기  시작 ---------------------------------------------------------------
    if category =="shirt":
        overlay = cv2.resize(overlay, dsize=(400,450))
        h, w ,c = overlay.shape

        shapes = np.zeros_like(Backgrund, np.uint8)

        shapes[0+200:h+200, 300+0:w+300] = overlay
        # cv2.imshow('shapes.png', shapes)
        # cv2.imshow('overlay.png', overlay)
        alpha = 0.5
        mask = shapes.astype(bool)
    elif category== "cap":
        overlay = cv2.resize(overlay, dsize=(400,300))
        h, w ,c = overlay.shape

        shapes = np.zeros_like(Backgrund, np.uint8)

        shapes[125+0:h+125, 250+0:w+250] = overlay
        alpha = 0.5
        mask = shapes.astype(bool)

    elif category=="Hood":
        overlay = cv2.resize(overlay, dsize=(300,250))
        h, w ,c = overlay.shape

        shapes = np.zeros_like(Backgrund, np.uint8)

        shapes[240+0:h+240, 200+0:w+200] = overlay
        alpha = 0.5
        mask = shapes.astype(bool)

    # # -------------------------------------업로드 이미지(.png) 배경 지우기 끝---------------------------------------------------------------
    # # -------------------------------------이미지 색상 변경 시작 ---------------------------------------------------------------

    # # -------------------------------------이미지 색상 변경 끝 ---------------------------------------------------------------
    # Backgrund[mask] = shapes[mask]
    Backgrund[mask] = cv2.addWeighted(shapes, alpha, shapes, 1 - alpha, 0)[mask]
    url=img_read.split("/")[-1]
    cv2.imwrite("media/output/"+url,Backgrund)


