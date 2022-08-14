#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class mecab(unittest.TestCase):

    def test(self):
        import termextract.mecab
        import termextract.core
        f = open("../test_data/mecab_out_sample.txt", "r", encoding="utf-8")
        tagged_text = f.read()
        f.close()
        frequency = termextract.mecab.cmp_noun_dict(tagged_text)
        lr = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.mecab.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        self.assertIn("人工 知能 技術", frequency)
        self.assertEqual(round(lr["知能"],2), 18.14)

if __name__ == '__main__':
    unittest.main()
