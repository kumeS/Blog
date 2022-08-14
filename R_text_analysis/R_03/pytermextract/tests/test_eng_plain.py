#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class eng_plaintext(unittest.TestCase):

    def test(self):
        import termextract.english_plaintext
        import termextract.core
        f = open("../test_data/eng_sample.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        frequency = termextract.english_plaintext.cmp_noun_dict(text)
        lr = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.english_plaintext.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        self.assertIn("central property of humans", frequency)
        self.assertEqual(round(lr["digital technology"],2), 2.83)

if __name__ == '__main__':
    unittest.main()
