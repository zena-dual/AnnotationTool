#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter
import tkFont
from ScrolledText import *


# タグと属性の組み合わせをresource/tag_attributeから読み込む関数
# tag_list: タグ名のリスト
# attribute_dict: キーとしてタグ名、値として属性を持つ辞書
tag_list = []
attribute_dict = {}
def read_tag_and_attribute():
    tag_attribute = open("resource/tag_attribute", "r")
    
    for line in tag_attribute:
        string = line.replace("\n", "").split(",")
        tag_list.append(string[0])
        if len(line) > 1:
            attribute_dict[string[0]] = []
            i = 1
            while i < len(string):
                attribute_dict[string[0]].append(string[i])
                i += 1
    
    return tag_list, attribute_dict


# 左側のテキストをドラッグで選択し、選択したテキストを右側のテキストに送る関数
def index_capture(hoge):
    t1.insert(Tkinter.END,t0.get(t0.index(Tkinter.SEL_FIRST),\
                                 t0.index(Tkinter.SEL_LAST)))
    t1.insert(Tkinter.END, "\t")
    t1.insert(Tkinter.END, "hoge")
    t1.insert(Tkinter.END, "\n")
    

if __name__ == "__main__":
    file_name = "resource/" + sys.argv[1]
    text = open(file_name, "r")

    root = Tkinter.Tk()
    # 実行処理はここから
    
    root.title("Software Title")
    root.geometry("1200x600")

    # 左側のテキストがファイルの出力兼アノテーションの対象
    # 右側のテキストがアノテーションの出力
    font = tkFont.Font(size=14)
    t0 = ScrolledText(width=70,font=font,background="#fffff0")
    t1 = ScrolledText(width=70,font=font,background="#fffff0")
    t0.place(x=10,y=10)
    t1.place(x=600,y=10)

    # 左側のテキストにファイルの内容を反映
    for element in text:
        t0.insert(Tkinter.END, "　" + element)

    # ドラッグ時の挙動をbind
    t0.bind("<ButtonRelease>", index_capture)

    # "Choose tag to annotate"ラベルを表示
    tagID = Tkinter.IntVar()
    tagID.set(0)
    TagChoiceLabel = Tkinter.Label(text="Choose tag to annotate",\
                                   background="#b0c4de")
    TagChoiceLabel.place(x=70,y=430)

    # アノテーションするタグの選択
    read_tag_and_attribute()
    tag_rb_list = []
    i = 0
    X_rb = -180
    Y_rb = 455
    while i < len(tag_list):
        # ラジオボタンの位置調整
        if i % 5 == 0:
            X_rb += 190
            Y_rb = 455
        
        tag_rb_list.append(Tkinter.Radiobutton(text = tag_list[i],\
                                               variable = tagID,\
                                               value = i))
        tag_rb_list[i].place(x=X_rb,y=Y_rb)
        Y_rb += 20
        i += 1

    # 実行処理はここまで
    root.mainloop()
