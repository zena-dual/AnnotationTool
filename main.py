#!/usr/bin/env python
# -*- coding: utf-8 -*-

index = ""

if __name__ == "__main__":
    import sys
    import Tkinter
    import tkFont
    from ScrolledText import *
    
    file_name = "resource/" + sys.argv[1]
    text = open(file_name, "r")

    root = Tkinter.Tk()
    # 実行処理はここから
    
    root.title("Software Title")
    root.geometry("1200x600")

    # 左側のテキストがファイルの出力
    # 右側のテキストがアノテーションの対象
    font = tkFont.Font(size=14)
    t0 = ScrolledText(width=70,font=font)
    t1 = ScrolledText(width=70,font=font)
    t0.place(x=10,y=10)
    t1.place(x=600,y=10)
    for element in text:
        t0.insert(Tkinter.END, element)

    # 1回クリックした文字からもう1回クリックした文字までを右側のテキストに送る
    def index_capture(hoge):
        global index
        if index == "":
            index = t0.index(Tkinter.CURRENT)
        else:
            t1.insert(Tkinter.END, t0.get(index, t0.index(Tkinter.CURRENT)))
            t1.insert(Tkinter.END, "\t")
            t1.insert(Tkinter.END, "hoge")
            t1.insert(Tkinter.END, "\n")
            index = ""
    t0.bind("<ButtonRelease>", index_capture)

    # 実行処理はここまで
    root.mainloop()
