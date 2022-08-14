#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_chi_plain.py chinese_text.txt

　・引数に入力とする中文テキストファイル(utf8)を指定
　・処理結果ファイル: 　nlpir_extracted.txt

 　本パッケージ中のテストデータを使う例は以下
 　python termex_chi_plain.py ../test_data/chi_sample_s.txt

"""

import sys
import collections

import termextract.core
import termextract.chinese_plaintext

def output(data):
    """
    処理結果を"chi_plain_extracted.txt"に出力
    """
    outfile = open("chi_plain_extracted.txt", "w", encoding="utf-8")
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
    frequency = termextract.chinese_plaintext.cmp_noun_dict(text)
    # term_list = termextract.chinese_plaintext.cmp_noun_list(text)
    lr = termextract.core.score_lr(
        frequency,
        ignore_words=termextract.chinese_plaintext.IGNORE_WORDS,
        lr_mode=1, average_rate=1)
    term_imp = termextract.core.term_importance(frequency, lr)
    output(term_imp)
