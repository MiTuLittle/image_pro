#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#功能实现函数

import math
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import cv2


class ImageCompressUtil(object):
    # 等比例压缩
    def resizeImg(self, **args):
        try:
            args_key = {'ori_img': '', 'dst_img': '',
                        'dst_w': '', 'dst_h': '', 'save_q': 100}
            arg = {}
            for key in args_key:
                if key in args:
                    arg[key] = args[key]
            im = Image.open(arg['ori_img'])
            if im.format in ['gif', 'GIF', 'Gif']:
                return
            ori_w, ori_h = im.size
            widthRatio = heightRatio = None
            ratio = 1
            if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
                if arg['dst_w'] and ori_w > arg['dst_w']:
                    widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
                if arg['dst_h'] and ori_h > arg['dst_h']:
                    heightRatio = float(arg['dst_h']) / ori_h
                if widthRatio and heightRatio:
                    if widthRatio < heightRatio:
                        ratio = widthRatio
                    else:
                        ratio = heightRatio
                if widthRatio and not heightRatio:
                    ratio = widthRatio
                if heightRatio and not widthRatio:
                    ratio = heightRatio
                newWidth = int(ori_w * ratio)
                newHeight = int(ori_h * ratio)
            else:
                newWidth = ori_w
                newHeight = ori_h
            if len(im.split()) == 4:
                # prevent IOError: cannot write mode RGBA as BMP
                r, g, b, a = im.split()
                im = Image.merge("RGB", (r, g, b))
            #im.resize((newWidth, newHeight), Image.ANTIALIAS).save(
                #arg['dst_img'], quality=arg['save_q'])
            imresize = im.resize((newWidth, newHeight), Image.ANTIALIAS)
            return imresize
        except Exception as e:
            #LogDao.warn(u'压缩失败' + str(e), belong_to='resizeImg')
            print(e)
            #pass

    #指定尺寸压缩（物体不变形）
    def fillPic(self, **args1):
        try:
            args_key = {'resizePic': '', 'dst_w1': '',
                        'dst_h1': ''}
            arg = {}
            for key in args_key:
                if key in args1:
                    arg[key] = args1[key]
            image_fill = arg['resizePic']
            ori_w1, ori_h1 = image_fill.size
            speci_w = arg['dst_w1']
            speci_h = arg['dst_h1']
            judge_w = ori_w1 - speci_w
            judge_h = ori_h1 - speci_h
            if judge_w != 0 or judge_h != 0:
                #缩减
                if judge_w >= 0 and judge_h >= 0:
                    #print("缩减")
                    imageArray_fill = np.array(image_fill)
                    image_fill = imageArray_fill[math.ceil(judge_h/2):int(ori_h1 - int(judge_h/2)),math.ceil(judge_w/2):int(ori_w1 - int(judge_w/2))]
                    image_fill = Image.fromarray(image_fill)
                #填充
                elif judge_w <= 0 and judge_h <= 0:
                    #print("填充")
                    judge_w = abs(judge_w)
                    judge_h = abs(judge_h)
                    imageArray_fill = np.array(image_fill)
                    image_fill = cv2.copyMakeBorder(imageArray_fill, math.ceil(
                        judge_h/2), int(judge_h/2), math.ceil(judge_w/2), int(judge_w/2), cv2.BORDER_REPLICATE)
                    image_fill = Image.fromarray(image_fill)
                return image_fill
            else:
                return image_fill
        except Exception as e:
            print(e)
            #pass
    
    #文件夹是否存在校验
    def mkdir(self,path):     
        # 去除首位空格
        path=path.strip()
        
        # 去除尾部 \ 符号
        path=path.rstrip("\\")
    
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
    
        # 判断结果
        if not isExists:
            os.makedirs(path)
            #print(path+' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            #print(path+' 目录已存在')
            return False


def main():
    # 目标图片大小
    dst_w = 500  # int(sys.argv[1])
    dst_h = 700  # int(sys.argv[2])
    # 保存的图片质量
    save_q = 100  # int(sys.argv[3])
    #图片读取和保存路径
    srcPath = 'D:\\picSet\\cutPic\\src\\038CC1F028-5-1.jpg'
    savePath = 'D:\\picSet\\cutPic\\src\\YSDXTEST\\save1-1-' + \
        str(save_q) + '.jpg'

    if os.path.exists(srcPath) and len(os.path.basename(srcPath).split('.')) > 1:

        image_chang = ImageCompressUtil().resizeImg(
            ori_img=srcPath,
            dst_img=savePath,
            dst_w=dst_w,
            dst_h=dst_h,
            save_q=save_q
        )
        plt.imshow(image_chang)
        plt.show()
        if dst_h == 0 or dst_w == 0:
            pass
        else:
            image_chang = ImageCompressUtil().fillPic(
                resizePic=image_chang, dst_w1=dst_w, dst_h1=dst_h)
        if image_chang is None:
            print("失败")
            return
        print("结束")
        image_chang.save(savePath, quality=save_q)
    else:
        print("图片不存在")


if __name__ == '__main__':
    main()
