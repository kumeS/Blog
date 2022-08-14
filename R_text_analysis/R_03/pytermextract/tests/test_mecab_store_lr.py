#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class mecab_dbm(unittest.TestCase):

    def test(self):
        import dbm
        import termextract.mecab
        import termextract.core

        f = open("../test_data/mecab_out_sample.txt", "r", encoding="utf-8")
        tagged_text = f.read()
        f.close()
        DB = dbm.open("store-lr", "n")
        frequency = termextract.mecab.cmp_noun_dict(tagged_text)
        termextract.core.store_lr(frequency, dbm=DB)
       
        lr = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.mecab.IGNORE_WORDS,
            lr_mode=1, average_rate=1, dbm=DB)
        DB.close()
        self.assertIn("人工 知能 技術", frequency)
        self.assertEqual(round(lr["知能"],2), 18.14)

if __name__ == '__main__':
    unittest.main()
