#!/usr/bin/env python
# coding=utf-8
import os,re
# 列出当前目录下所有的文件
files = os.listdir(".")
for filename in files:
    portion = os.path.splitext(filename)
    # 如果后缀是.vtt
    if portion[1] == ".vtt":
        # 重新组合文件名和后缀名files = os.listdir(".")
        newname = portion[0] + ".txt"
        os.rename(filename,newname)

files = os.listdir(".")
for filename in files:
    portion = os.path.splitext(filename)
    # 如果后缀是.txt
    if portion[1] == ".txt":
        with open(filename,'rt+') as f:
            date=f.read()
            date=date.replace('<v Chinese>','')
            date=date.replace('</v>','')
            f.seek(0)
            f.write(date)
        newname = portion[0] + ".srt"
        os.rename(filename,newname)
