import unittest

import bleu
from bleu.tests.data import REF_FILES, TRANS_FILES
from bleu.utils import load_reference_corpus, load_translation_corpus


class TestMetrics(unittest.TestCase):
    reference_corpus = load_reference_corpus(REF_FILES)

    def test_corpus_level(self):
        scores = [
            bleu.bleu_corpus_level(
                translation_corpus=load_translation_corpus(file),
                reference_corpus=self.reference_corpus,
            ).bleu
            for file in TRANS_FILES
        ]

        self.assertGreater(scores[1], scores[0], msg='score2 should be better than score1')

    def test_sentence_level(self):
        trans = TRANS_FILES[0]
        trans_corpus = load_translation_corpus(trans)

        sentence_score = bleu.bleu_sentence_level(
            translation_sentence=trans_corpus[0],
            reference_corpus=self.reference_corpus[0],
        )
        corpus_score = bleu.bleu_corpus_level(
            translation_corpus=trans_corpus,
            reference_corpus=self.reference_corpus,
        )

        self.assertAlmostEqual(
            sentence_score,
            corpus_score,
            msg="""
            sentence_score: %r
            corpus_score: %r
            """ % (sentence_score, corpus_score)
        )

    def test_smooth(self):
        translation_corpus = ['this sentence only has unigram matches'.split()]
        reference_corpus = [[
            'matches unigram has only sentence this'.split()
        ]]

        score = bleu.bleu_corpus_level(translation_corpus, reference_corpus)
        self.assertAlmostEqual(score.bleu, 0.0, msg='get 0 without smoothing')

        score = bleu.bleu_corpus_level(translation_corpus, reference_corpus, smooth=True)
        self.assertGreater(score.bleu, 0.0, msg='get non-zero after smoothing')
