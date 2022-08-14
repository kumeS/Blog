#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class janome(unittest.TestCase):

    def test(self):
        from janome.tokenizer import Tokenizer
        import termextract.janome
        import termextract.core
        f = open("../test_data/jpn_sample.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        t = Tokenizer()
        tokenize_text = t.tokenize(text)
        frequency = termextract.janome.cmp_noun_dict(tokenize_text)
        lr = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.janome.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        self.assertIn("人工 知能 技術", frequency)
        self.assertEqual(round(lr["知能"],2),18.14)

if __name__ == '__main__':
    unittest.main()
