#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_janome_pp.py japanese_text.txt

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・処理結果ファイル: 　janome_extracted_pp.txt
　
 　本パッケージ中のテストデータを使う例は以下
 　python termex_janome_pp.py ../test_data/jpn_sample.txt

"""

import sys
import collections
import dbm

from janome.tokenizer import Tokenizer
import termextract.janome
import termextract.core

def output(data):
    """
    処理結果を"janome_extracted_pp.txt"に出力
    """
    outfile = open("janome_extracted_pp.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        outfile.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        outfile.write("\t")
        outfile.write(str(value))
        outfile.write("\n")
    outfile.close()

if __name__ == "__main__":
    ARGVS = sys.argv
    infile = open(ARGVS[1], "r", encoding="utf-8")
    text = infile.read()
    infile.close()
    t = Tokenizer()
    tokenize_text = t.tokenize(text)
    frequency = termextract.janome.cmp_noun_dict(tokenize_text)
    #term_list = termextract.mecab.cmp_noun_list(tagged_text)
    term_imp = termextract.core.score_pp(
        frequency,
        ignore_words=termextract.mecab.IGNORE_WORDS,
        average_rate=1)
    output(term_imp)
