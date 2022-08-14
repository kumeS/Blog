#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class nlpir(unittest.TestCase):

    def test(self):
        import pynlpir
        import termextract.nlpir
        import termextract.core
        f = open("../test_data/chi_sample.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        pynlpir.open()
        text = text.replace('\n',' ') # 改行は削除しておく
        tagged_text = pynlpir.segment(text)
        frequency = termextract.nlpir.cmp_noun_dict(tagged_text)
        LR = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.nlpir.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        self.assertIn("世界 模型", frequency)
        self.assertEqual(round(LR["弱 人工智能"],2), 2.34)

if __name__ == '__main__':
    unittest.main()
