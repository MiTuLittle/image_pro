函数解释


脚本调用函数：

1. fillBland.py 空白填充函数，参数1：指定目标图片宽度（必填）；
                             参数2：指定目标图片高度（必填）；
                             参数3：源图片路径（必填）；
                             参数4：图片保存路径（必填）

2. extraCutting.py 多余裁剪函数，参数1：指定目标图片宽度（必填）；
                                参数2：指定目标图片高度（必填）；
                                参数3：源图片路径（必填）；
                                参数4：图片保存路径（必填）

3. high_adapte.py 高度适配函数， 参数1：指定目标图片高度（必填）；
                                参数2：源图片路径（必填）；
                                参数3：图片保存路径（必填）

4. width_adapte.py 宽度适配函数，参数1：指定目标图片宽度（必填）；
                                参数2：源图片路径（必填）；
                                参数3：图片保存路径（必填）

功能函数：

picSizeChang.py 功能函数，上述四个函数调用该函数，实现图片的等比例压缩并根据参数实现空白填充、多余裁剪、高度适配、宽度适配.