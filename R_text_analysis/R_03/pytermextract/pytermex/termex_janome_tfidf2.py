#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python termex_janome_tfidf2.py 01.txt

　・引数に入力とする日本語テキストファイル(utf8)を指定
　・集計済みIDFをもとに、引数で与えたテキストファイルの
　　用語重要度を出力
　・処理結果ファイル: 　janome_extracted-tfidf.txt
　
 　本パッケージ中のテストデータを使う例は以下
 　python termex_janome_tfidf2.py ../test_data/jpn_sample.txt

"""

import sys
import collections
import dbm

from janome.tokenizer import Tokenizer
import termextract.janome
import termextract.core

def output(data):
    """
    処理結果を"janome_extracted-tfidf.txt"に出力
    """
    outfile = open("janome_extracted-tfidf.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        outfile.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        outfile.write("\t")
        outfile.write(str(value))
        outfile.write("\n")
    outfile.close()

if __name__ == "__main__":
    t = Tokenizer()
    # 処理対象のテキスト（事前にDFに読み込ませる必要あり）を呼び出し
    ARGVS = sys.argv
    infile = open(ARGVS[1], "r", encoding="utf-8")
    text = infile.read()
    infile.close()
    tokenize_text = t.tokenize(text)
    frequency = termextract.janome.cmp_noun_dict(tokenize_text)

    # FerequencyからTFを生成する
    tf = termextract.core.frequency2tf(frequency)

    # 蓄積したDF情報からIDFを呼び出し。
    DF = dbm.open("df", "r")
    idf = termextract.core.get_idf(frequency, dbm=DF)
    DF.close()

    # 重要度をTFとIDFの組み合わせとし、ファイル出力
    term_imp = termextract.core.term_importance(tf, idf)
    output(term_imp)
