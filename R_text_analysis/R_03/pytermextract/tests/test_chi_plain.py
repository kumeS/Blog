#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class chinese_plaintext(unittest.TestCase):

    def test(self):
        import termextract.chinese_plaintext
        import termextract.core
        f = open("../test_data/chi_sample_s.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        frequency = termextract.chinese_plaintext.cmp_noun_dict(text)
        lr = termextract.core.score_lr(
            frequency,
            ignore_words=termextract.chinese_plaintext.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        #self.assertIn("符 合 格 式 手 冊 規範", frequency)
        self.assertEqual(round(lr["计 算 机 科 學"],2), 1.94)

if __name__ == '__main__':
    unittest.main()
