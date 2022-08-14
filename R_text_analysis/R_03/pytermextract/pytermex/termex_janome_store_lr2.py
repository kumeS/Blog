#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_janome_store_lr2.py 01.txt

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・事前学習結果をもとに、引数で与えたテキストファイルの
　　用語重要度を出力
　・処理結果ファイル: 　janome_extracted-store_lr.txt

 　本パッケージ中のテストデータを使う例は以下
 　python termex_janome_store_lr2.py ../test_data/jpn_sample.txt

"""

import sys
import collections
import dbm

from janome.tokenizer import Tokenizer
import termextract.janome
import termextract.core

def output(data):
    """
    処理結果を"janome_extracted-store_lr.txt"に出力
    """
    outfile = open("janome_extracted-store_lr.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        outfile.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        outfile.write("\t")
        outfile.write(str(value))
        outfile.write("\n")
    outfile.close()

if __name__ == "__main__":
    ARGVS = sys.argv
    t = Tokenizer()
    # 専門用語抽出対象の文書を読み込み
    infile = open(ARGVS[1], "r", encoding="utf-8")
    text = infile.read()
    infile.close()
    tokenize_text = t.tokenize(text)
    frequency = termextract.janome.cmp_noun_dict(tokenize_text)

    # 蓄積したLR情報からLRを呼び出し
    DB = dbm.open("store-lr", "r")
    lr = termextract.core.score_lr(
        frequency,
        ignore_words=termextract.janome.IGNORE_WORDS,
        lr_mode=1, average_rate=1, dbm=DB)
    DB.close()

    # 重要度をfrequencyとLRの組み合わせとし、ファイル出力
    term_imp = termextract.core.term_importance(frequency, lr)
    output(term_imp)
