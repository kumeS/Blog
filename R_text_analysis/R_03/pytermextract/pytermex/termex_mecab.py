#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_mecab.py mecab_tagged.txt

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・集計済みIDFをもとに、引数で与えたテキストファイルの
　　用語重要度を出力
　・処理結果ファイル: 　"mecab_extracted.txt"
　
 　本パッケージ中のテストデータを使う例は以下
 　python termex_mecab.py ../test_data/mecab_out_sample.txt
  
"""

import sys
import collections
import dbm

import termextract.mecab
import termextract.core

def output(data):
    """
    処理結果を"mecab_extracted.txt"に出力
    """
    outfile = open("mecab_extracted.txt", "w", encoding="utf-8")
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
    tagged_text = infile.read()
    infile.close()

    frequency = termextract.mecab.cmp_noun_dict(tagged_text)
    #term_list = termextract.mecab.cmp_noun_list(tagged_text)
    lr = termextract.core.score_lr(
        frequency,
        ignore_words=termextract.mecab.IGNORE_WORDS,
        lr_mode=1, average_rate=1)
    term_imp = termextract.core.term_importance(frequency, lr)
    output(term_imp)
