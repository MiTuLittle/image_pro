#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#空白填充函数

import os
import sys

import numpy as np
from PIL import Image

from picSizeChange import ImageCompressUtil


def main():
    # 目标图片大小
    dst_wm = int(sys.argv[1])
    dst_hm = int(sys.argv[2])
    # 保存的图片质量
    save_q = 100
    #图片读取和保存路径
    srcPath = sys.argv[3]
    savePath = sys.argv[4]
    if dst_hm is None or srcPath is None or savePath is None or dst_wm is None:
        return
    h_ext = 0
    w_ext = 0
    if not os.path.exists(savePath):
        path_get = os.path.dirname(savePath)
        ImageCompressUtil().mkdir(path_get)
    if os.path.exists(srcPath) and len(os.path.basename(srcPath).split('.')) > 1:

        im_j = Image.open(srcPath)
        if im_j.format in ['gif', 'GIF', 'Gif']:
            return
        ori_w_j, ori_h_j = im_j.size
        w_ratio = dst_wm / ori_w_j
        h_ratio = dst_hm / ori_h_j

        if h_ratio * ori_w_j < dst_wm or h_ratio * ori_h_j < dst_hm:
            h_ext = dst_hm
            w_ext = 0
        elif w_ratio * ori_w_j < dst_wm or w_ratio * ori_h_j < dst_hm:
            h_ext = 0
            w_ext = dst_wm
        image_chang = ImageCompressUtil().resizeImg(
            ori_img=srcPath,
            dst_img=savePath,
            dst_w=int(w_ext),
            dst_h=int(h_ext),
            save_q=save_q
        )
        if dst_hm == 0 or dst_wm == 0:
            pass
        else:
            image_chang = ImageCompressUtil().fillPic(
                resizePic=image_chang, dst_w1=dst_wm, dst_h1=dst_hm)
        if image_chang is None:
            print("失败")
            return
        print("结束")
        image_chang.save(savePath, quality=save_q)
    else:
        print("图片不存在")


if __name__ == "__main__":
    main()
