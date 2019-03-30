import unittest

from bleu.tests.data import TRANS_FILES, REF_FILES, N_TEST_REF
from bleu.utils import load_translation_corpus, load_reference_corpus


class TestUtils(unittest.TestCase):

    def test_load_translation_corpus(self):
        for file in TRANS_FILES:
            trans_corpus = load_translation_corpus(file)
            self.assertEqual(len(trans_corpus), 1)
            self.assertTrue(isinstance(trans_corpus[0], list))

    def test_load_reference_corpus(self):
        ref_corpus = load_reference_corpus(REF_FILES)
        self.assertEqual(len(ref_corpus), 1, msg='ref_corpus for only one trans')
        refs = ref_corpus[0]
        self.assertEqual(len(refs), N_TEST_REF, msg='3 references for one trans')
