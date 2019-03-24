import unittest
import bleu.tests as tests
import bleu.metrics as bleu


class TestBleu(unittest.TestCase):

    def test_basic(self):
        scores = [
            bleu.compute_bleu(trains, tests.reference_corpus).bleu
            for trains in tests.translation_corpus
        ]

        self.assertGreater(scores[1], scores[0], msg='score2 is better than score1')

    def test_smooth(self):
        translation_corpus = ['this sentence only has unigram matches'.split()]
        reference_corpus = [[
            'matches unigram has only sentence this'.split()
        ]]

        score = bleu.compute_bleu(translation_corpus, reference_corpus)
        self.assertAlmostEqual(score.bleu, 0.0, msg='get 0 without smoothing')
        score = bleu.compute_bleu(translation_corpus, reference_corpus, smooth=True)
        self.assertGreater(score.bleu, 0.0, msg='after smoothing')
