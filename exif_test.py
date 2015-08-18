#!/usr/bin/python
# -*- coding:utf-8 -*-
import exifread
import json


def get_exif(file_path):
    f = open(file_path, 'rb')
    tag1 = exifread.process_file(f, details=False, strict=True)
    tag = {}
    for key, value in tag1.items():
            if key not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                tag[key] = str(value)
                print "%s, %s" % (key, value) #打印数据检验tag{}储存的是否相同
    tags = json.dumps(tag)
    return tags
file_path = raw_input()
print get_exif(file_path)
