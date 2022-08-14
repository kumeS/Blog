#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class english_postagger(unittest.TestCase):

    def test(self):
        import nltk
        import termextract.english_postagger
        import termextract.core
        f = open("../test_data/eng_sample.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
        tagged_text = nltk.pos_tag(nltk.word_tokenize(text))
        frequency  = termextract.english_postagger.cmp_noun_dict(tagged_text)
        lr = termextract.core.score_lr(
            frequency, 
            ignore_words=termextract.english_postagger.IGNORE_WORDS,
            lr_mode=1, average_rate=1)
        term_imp = termextract.core.term_importance(frequency, lr)
        self.assertEqual(round(lr["digital technology"],2), 3.72)

if __name__ == '__main__':
    unittest.main()
