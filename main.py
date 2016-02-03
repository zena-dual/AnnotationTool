#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter
import Tag
import tkFont
from ScrolledText import *
import json


# タグと属性の組み合わせをresource/tag_attributeから読み込む関数
tag_list = []
def read_tag_and_attribute():
    tag_attribute = open("resource/tag_attribute", "r")    
    for line in tag_attribute:
        string = line.replace("\n", "").split(",")
        tag_list.append(string)
        

def annotate(hoge):
    t1.insert(Tkinter.END,t2.get() + "\n")


# アノテーションの結果をjson形式にして出力
output_text = []
output_dict = {}
def stringize(hoge):
    i = 0
    index = t1.index(Tkinter.END).split(".")
    while i < int(index[0]):
        start = str(i+1) + ".0"
        end = str(i+1) + ".end"
        if t1.get(start,end) != "":
            output_text.append(t1.get(start,end))
        i += 1
    for element in output_text:
        value_dict = {}
        elem_list = element.split(",")
        i = 1
        while i < len(elem_list):
            attr = elem_list[i]
            value_dict[attr.split(":")[0]] = attr.split(":")[1]
            i += 1
        output_dict[elem_list[0]] = value_dict
    output_json = json.dumps(output_dict, indent=4)
    output.write(output_json)
    

if __name__ == "__main__":
    input_filename = "resource/" + sys.argv[1] + ".txt"
    output_filename = "result/" + sys.argv[1] + ".json"
    text = open(input_filename, "r")
    output = open(output_filename, "w")

    root = Tkinter.Tk()
    # 実行処理はここから
    
    root.title("Software Title")
    root.geometry("1200x700")
    tagID = Tkinter.IntVar()
    tagID.set(0)
    font = tkFont.Font(size=14)
    
    # t0: ファイルの出力兼アノテーションの対象
    # t1: アノテーションの出力
    # t2: アノテーション途中のテキスト
    # confirm: アノテーションを確定させるボタン
    t0 = ScrolledText(width=70,font=font,background="#fffff0")
    t1 = ScrolledText(width=70,font=font,background="#fffff0")
    t2 = Tkinter.Entry(width=140)
    confirm = Tkinter.Button(text="confirm annotation")
    finish = Tkinter.Button(text="finish annotation")
    TagChoiceLabel = Tkinter.Label(text="Choose tag to annotate", background="#b0c4de")
    t0.place(x=10,y=10)
    t1.place(x=600,y=10)
    t2.place(x=10,y=610)
    confirm.place(x=530,y=640)
    confirm.bind("<ButtonRelease>",annotate)
    finish.place(x=537,y=665)
    finish.bind("<ButtonRelease>",stringize)
    TagChoiceLabel.place(x=525,y=430)

    # 左側のテキストにファイルの内容を反映
    for element in text:
        t0.insert(Tkinter.END, "　" + element)

    # アノテーションするタグの選択
    read_tag_and_attribute()
    tag_rb_list = []
    i = 0
    X = 10
    while i < len(tag_list):
        tag_rb_list.append(Tag.TagRB(tag_list[i], tagID, i, X, t0, t2))
        X += 120
        i += 1

    # 実行処理はここまで
    root.mainloop()
