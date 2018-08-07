#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#宽度适配函数

import os
import sys

from picSizeChange import ImageCompressUtil


def main():
    pass
    # 目标图片大小
    dst_w = int(sys.argv[1])
    dst_h = 0  # int(sys.argv[2])
    # 保存的图片质量
    save_q = 100  # int(sys.argv[3])
    #图片读取和保存路径
    srcPath = sys.argv[2]#'D:\\picSet\\cutPic\\src\\1905.jpg'
    savePath = sys.argv[3]#'D:\\picSet\\cutPic\\src\\YSDXTEST\\save1-1-' + str(save_q) + '.jpg'
    if dst_h is None or srcPath is None or savePath is None:
        return
    if not os.path.exists(savePath):
        path_get = os.path.dirname(savePath)
        ImageCompressUtil().mkdir(path_get)
    if os.path.exists(srcPath) and len(os.path.basename(srcPath).split('.')) > 1:
        image_chang = ImageCompressUtil().resizeImg(
            ori_img=srcPath,
            dst_img=savePath,
            dst_w=dst_w,
            dst_h=dst_h,
            save_q=save_q
        )
        if image_chang is None:
            print("失败")
            return
        print("结束")
        image_chang.save(savePath, quality=save_q)
    else:
        print("图片不存在")

if __name__ == "__main__":
    main()