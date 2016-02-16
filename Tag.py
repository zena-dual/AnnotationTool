#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk

tag_num = {}
attr_dict = {}
instance_list = []
ID_dict = {}
entry_dict = {}

# タグと属性を書いたオブジェクトを配置する
# 座標は適当
def place(instance):
    instance.tag_rb.place(x=900,y=instance.mY)

    
def read_attribute_and_value():
    attr_value = open("resource/attribute_value", "r")
    for line in attr_value:
        if len(line.split(",")) > 1:
            string = line.replace("\n", "").split(",")
            string.pop(0)
            attr_dict[line.split(",")[0]] = string
            

def get_id():
    return ID_dict


def get_entry():
    return entry_dict


# タグが選択された時、その属性と値を記述するウィジェットを配置する
def tag_selected(tag):
    global instance_list, ID_dict, entry_dict
    # ウィジェットを削除するメソッドがないの意味不明じゃない？
    # ウィジェットのインスタンスを削除できないので画面外に置いてなかったことにする
    # メモリが死にそう
    for elem in instance_list:
        elem.place(x=1000000,y=1000000)
    instance_list = []
    ID_dict = {}
    entry_dict = {}
        
    i = 0
    for elem in tag.mAttribute:
        label = tk.Label(text=elem,width=13)
        label.place(x=10+i*120,y=450)
        instance_list.append(label)

        if elem in attr_dict.keys():
            ID = tk.StringVar()
            ID.set("null")
            ID_dict[elem] = ID
            j = 0
            for v in attr_dict[elem]:
                rb = tk.Radiobutton(text=v,variable=ID,value=v)
                rb.place(x=10+i*120,y=475+j*25)
                instance_list.append(rb)
                j += 1
        else:
            entry = tk.Entry(width=12)
            entry.place(x=10+i*120,y=475)
            entry_dict[elem] = entry
            instance_list.append(entry)
        i += 1

        
class TagRB:
    # タグのラジオボタンに関するクラス
    def __init__(self, tag_list, tagID, ID):
        # 初期化
        self.mTagName = tag_list[0]
        self.mTag = tag_list[1]
        self.mY = 10 + ID * 25
        
        self.mAttribute = []
        i = 2
        while i < len(tag_list):
            self.mAttribute.append(tag_list[i])
            i += 1

        global tag_num
        tag_num[self.mTag] = 1

        global attr_dict
        read_attribute_and_value()

        #インスタンス生成
        self.tag_rb = tk.Radiobutton(text=self.mTagName,variable=tagID,value=ID)

