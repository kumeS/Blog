#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_janome_store_lr1.py 01.txt 02.txt ...

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・入力に指定したすべてのテキストファイルから学習
　・集計結果はdbm "store-lr"に蓄積

 　本パッケージ中のテストデータを使う例は以下
 　python termex_janome_store_lr1.py ../test_data/jpn_sample.txt
 　   ../test_data/jpn_sample2.txt
 　   ../test_data/jpn_sample3.txt

"""

import sys
import dbm

from janome.tokenizer import Tokenizer
import termextract.janome
import termextract.core

if __name__ == "__main__":
    ARGVS = sys.argv
    # LRの情報を蓄積（事前処理）
    DB = dbm.open("store-lr", "c")
    input_files = ARGVS[1:]
    t = Tokenizer()
    for file in input_files:
        f = open(file, "r", encoding="utf-8")
        text = f.read()
        f.close()
        tokenize_text = t.tokenize(text)
        frequency = termextract.janome.cmp_noun_dict(tokenize_text)
        termextract.core.store_lr(frequency, dbm=DB)
    DB.close()
