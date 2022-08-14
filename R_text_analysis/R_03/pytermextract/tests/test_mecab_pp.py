#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class MeCab_pp(unittest.TestCase):

    def test(self):
        import termextract.mecab
        import termextract.core
        f = open("../test_data/mecab_out_sample.txt", "r", encoding="utf-8")
        tagged_text = f.read()
        f.close()
        frequency = termextract.mecab.cmp_noun_dict(tagged_text)
        term_ipm = termextract.core.score_pp(
            frequency,
            ignore_words=termextract.mecab.IGNORE_WORDS,
            average_rate=1)
        self.assertIn("人工 知能 技術", frequency)
        self.assertEqual(round(term_ipm["知能"],2), 4.13)

if __name__ == '__main__':
    unittest.main()
