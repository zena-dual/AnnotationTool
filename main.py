#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter as tk
import Tag
import tkFont
from ScrolledText import *
import json


# タグと属性の組み合わせをresource/tag_attributeから読み込む関数
tag_list = []
tag_dict = {}
def read_tag_and_attribute():
    tag_attribute = open("resource/tag_attribute", "r")    
    for line in tag_attribute:
        string = line.replace("\n", "").split(",")
        tag_list.append(string)
        tag_dict[string[0]] = 1
        

# アノテーションの内容をt1に反映
def annotate(hoge):
    t1.insert(tk.END,t2.get() + "\n")
    tag_dict[tag_list[tagID.get()][0]] += 1


# アノテーションの結果をjson形式にして出力
output_text = []
output_dict = {}
def stringize(hoge):
    i = 0
    index = t1.index(tk.END).split(".")
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


# t2にアノテーションしたテキストを挿入する
def get_value(hoge):
    t2.delete(0, tk.END)
    if t0.tag_ranges(tk.SEL):
        t2.insert(tk.END, tag_list[tagID.get()][1] + \
                  str(tag_dict[tag_list[tagID.get()][0]]) + ",text:" + \
                  t0.get(t0.index(tk.SEL_FIRST), t0.index(tk.SEL_LAST)))
    else:
        t2.insert(tk.END, tag_list[tagID.get()][1] + \
                  str(tag_dict[tag_list[tagID.get()][0]]))
        
    ID_dict = Tag.get_id()
    entry_dict = Tag.get_entry()
    print entry_dict
    if len(ID_dict.keys()) > 0:
        for k,v in ID_dict.items():
            if v.get() != "null":
                t2.insert(tk.END, "," + k + ":" + v.get())
    if len(entry_dict.keys()) > 0:
        for k,v in entry_dict.items():
            t2.insert(tk.END, "," + k + ":" + v.get())
                

if __name__ == "__main__":
    input_filename = "resource/" + sys.argv[1] + ".txt"
    output_filename = "result/" + sys.argv[1] + ".json"
    text = open(input_filename, "r")
    output = open(output_filename, "w")

    root = tk.Tk()
    # 実行処理はここから
    
    root.title("Software Title")
    root.geometry("1200x800")
    tagID = tk.IntVar()
    tagID.set(-1)
    font = tkFont.Font(size=14)

    # t0: ファイルの出力兼アノテーションの対象
    # t1: アノテーションの出力
    # t2: アノテーション途中のテキスト
    # confirm: アノテーションを確定させるボタン
    # finish: アノテーション内容をjsonにするボタン
    t0 = ScrolledText(width=100,height=12,font=font,background="#fffff0")
    t1 = ScrolledText(width=100,height=12,font=font,background="#fffff0")
    t2 = tk.Entry(width=140)
    confirm = tk.Button(text="confirm annotation")
    submit = tk.Button(text="submit annotation")
    finish = tk.Button(text="finish annotation")
    t0.place(x=10,y=10)
    t1.place(x=10,y=230)
    t2.place(x=10,y=610)
    confirm.place(x=530,y=640)
    submit.place(x=533,y=665)
    finish.place(x=537,y=690)
    confirm.bind("<ButtonRelease>",get_value)
    submit.bind("<ButtonRelease>",annotate)
    finish.bind("<ButtonRelease>",stringize)

    # t0にファイルの内容を反映
    for element in text:
        t0.insert(tk.END, "　" + element)

    # アノテーションするタグの選択
    read_tag_and_attribute()
    tag_rb_list = []
    i = 0
    while i < len(tag_list):
        tag_rb_list.append(Tag.TagRB(tag_list[i], tagID, i))
        Tag.place(tag_rb_list[i])
        i += 1
    tag_confirm = tk.Button(text="choose tag")
    tag_confirm.place(x=900,y=10+i*25)
    def selected(hoge):
        Tag.tag_selected(tag_rb_list[tagID.get()])
    tag_confirm.bind("<ButtonRelease>",selected)

    # 実行処理はここまで
    root.mainloop()
