# MIT License
# 
# Copyright (c) 2019 Cong Feng.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
        self.assertEqual(len(ref_corpus), 1, msg="ref_corpus for only one trans")
        refs = ref_corpus[0]
        self.assertEqual(len(refs), N_TEST_REF, msg="3 references for one trans")
