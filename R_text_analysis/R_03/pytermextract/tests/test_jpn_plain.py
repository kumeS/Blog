#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class japanese_plaintext(unittest.TestCase):

    def test(self):
        import termextract.japanese_plaintext
        import termextract.core
        f = open("../test_data/jpn_sample.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        frequency = termextract.japanese_plaintext.cmp_noun_dict(text)
        lr = termextract.core.score_lr(frequency, lr_mode=1, average_rate=1)
        self.assertIn("大 学 入 試 センター", frequency)
        self.assertEqual(round(lr["行 動 型 システム"],2),6.73)

if __name__ == '__main__':
    unittest.main()
