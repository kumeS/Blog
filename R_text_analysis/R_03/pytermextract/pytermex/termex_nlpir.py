#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_nlpir.py chinese_text.txt

　・引数に入力とする中文テキストファイル(utf8)を指定
　・処理結果ファイル: 　nlpir_extracted.txt

 　本パッケージ中のテストデータを使う例は以下
 　python termex_nlpir.py ../test_data/chi_sample.txt

"""

import sys
import collections

import pynlpir
import termextract.nlpir
import termextract.core

def output(data):
    """
    処理結果を"eng_extracted.txt"に出力
    """
    outfile = open("nlpir_extracted.txt", "w", encoding="utf-8")
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
    pynlpir.open()
    text = text.replace('\n', ' ') # 改行は削除しておく
    tagged_text = pynlpir.segment(text)
    frequency = termextract.nlpir.cmp_noun_dict(tagged_text)
    # term_list = termextract.nlpir.cmp_noun_list(tagged_text)
    lr = termextract.core.score_lr(
        frequency,
        ignore_words=termextract.nlpir.IGNORE_WORDS,
        lr_mode=1, average_rate=1)
    term_imp = termextract.core.term_importance(frequency, lr)
    output(term_imp)
