#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter

tag_num = {}

# タグと属性を書いたオブジェクトを配置する
# 座標は適当
def place(instance):
    i = 20
    Y = 455
    instance.tag_rb.place(x=instance.mX,y=Y)
    for attr in instance.attribute_b:
        attr.place(x=instance.mX,y=Y+i)
        i += 25

class TagRB:
    def __init__(self, tag_list, tagID, ID, X, t0, t2):
        # タグのラジオボタンが選択された時の動作
        # タグとID、t0で選択されているテキストを結合してt2にぶちこむ
        # 選択されていない場合はタグとIDのみ
        def rb_selected():
            t2.delete(0,Tkinter.END)
            if t0.tag_ranges(Tkinter.SEL):
                t2.insert(Tkinter.END, self.mTag + str(tag_num[self.mTag]) + "," + \
                          "text:" + t0.get(t0.index(Tkinter.SEL_FIRST), t0.index(Tkinter.SEL_LAST)))
            else:
                t2.insert(Tkinter.END, self.mTag + str(tag_num[self.mTag]))
            tag_num[self.mTag] += 1

        # 属性のボタンが押された時の動作
        # 属性をまとめてt2にぶちこむ
        # 不要な属性までぶちこまれるのが玉に瑕
        def b_pressed():
            for element in self.mAttribute:
                t2.insert(Tkinter.END, "," + element + ":")

        # 初期化
        self.mTagName = tag_list[0]
        self.mTag = tag_list[1]
        self.mX = X
        self.mAttribute = []
        i = 2
        while i < len(tag_list):
            self.mAttribute.append(tag_list[i])
            i += 1

        # IDの更新
        # confirmしなくても増えるので変なIDになることもある
        global tag_num
        tag_num[self.mTag] = 1

        # インスタンス生成
        self.tag_rb = Tkinter.Radiobutton(text=self.mTagName,variable=tagID,value=ID,command=rb_selected)
        self.attribute_b = []
        i = 0
        while i < len(self.mAttribute):
            self.attribute_b.append(Tkinter.Button(text=self.mAttribute[i],command=b_pressed))
            i += 1

        #配置
        place(self)
