#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"测试使用pillow来处理图片信息"

from PIL import Image
image = Image.open("/Users/luyaoming/Pictures/小龙女.jpg")
print(image.format,image.size,image.mode)
image.thumbnail((200,300))
image.save("/Users/luyaoming/Pictures/thumb_小龙女.jpg","JPEG")