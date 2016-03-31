#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter as tk
import Tag
import tkFont
from ScrolledText import *
import json


# アノテーションの結果をjson形式にして出力
def stringize(hoge):
    output_file_json = "result/" + sys.argv[1] + ".json"
    output_file_txt = "result/" + sys.argv[1] + ".txt"

    output = open(output_file_txt, "w")
    text = t1.get(t1.index("1.0"), t1.index(tk.END))
    output.write(text.encode("utf-8"))
    output.close()
    
    output = open(output_file_json, "w")
    output_text = []
    output_dict = {}

    i = 0
    index = t1.index(tk.END).split(".")
    while i < int(index[0]):
        start = str(i+1) + ".0"
        end = str(i+1) + ".end"
        if t1.get(start,end) != "":
            output_text.append(t1.get(start,end).encode("utf-8"))
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
    output.close()

def confirm(hoge):
    t1.insert(t1.index(tk.INSERT), ",range:" + \
              t0.index(tk.SEL_FIRST) + "-" +t0.index(tk.SEL_LAST))
    
                

if __name__ == "__main__":
    input_txt = "resource/AnnotateTarget/" + sys.argv[1] + ".txt"
    input_json = "result/" + sys.argv[1] + ".txt"
    txt = open(input_txt, "r")
    jsn = open(input_json, "r+")

    root = tk.Tk()
    # 実行処理はここから
    
    root.title(sys.argv[1])
    root.geometry("850x550")
    font = tkFont.Font(size=14)

    # t0: 元テキスト
    # t1: json
    # b1: 範囲確定用ボタン
    # b2: 結果反映用ボタン
    t0 = ScrolledText(width=100,height=12,font=font,background="#fffff0")
    t1 = ScrolledText(width=100,height=12,font=font,background="#fffff0")
    b1 = tk.Button(text="confirm range")
    b2 = tk.Button(text="finish")
    t0.place(x=10,y=10)
    t1.place(x=10,y=230)
    b1.place(x=380,y=450)
    b2.place(x=406,y=475)
    b1.bind("<ButtonRelease>",confirm)
    b2.bind("<ButtonRelease>",stringize)

    # ファイルの内容を反映
    for element in txt:
        t0.insert(tk.END, element)

    for element in jsn:
        t1.insert(tk.END, element)

    # 実行処理はここまで
    root.mainloop()
