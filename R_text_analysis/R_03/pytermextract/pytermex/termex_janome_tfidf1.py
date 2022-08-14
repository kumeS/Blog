#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_janome_tfidf1.py 01.txt 02.txt ...

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・入力に指定したすべてのテキストファイルからDFを集計
　・集計結果はdbm "df"に蓄積
　
 　本パッケージ中のテストデータを使う例は以下
 　python termex_janome_tfidf1.py ../test_data/jpn_sample.txt
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
    # DF情報を蓄積
    input_files = ARGVS[1:]
    DF = dbm.open("df", "c")
    t = Tokenizer()
    for file in input_files:
        f = open(file, "r", encoding="utf-8")
        text = f.read()
        f.close()
        tokenize_text = t.tokenize(text)
        frequency = termextract.janome.cmp_noun_dict(tokenize_text)
        termextract.core.store_df(frequency, dbm=DF)
    DF.close()
