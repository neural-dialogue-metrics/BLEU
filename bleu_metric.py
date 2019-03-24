# Copyright 2019 Cong Feng. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Driver script to compute BLEU score."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import bleu


def _break_into_words(line):
    """
    Turn a already-tokenized line into a list of words.
    :param line: string, already tokenized. All tokens are separated by space.
    :return: List[string], broken into words.
    """
    return line.strip().split(' ')


def _read_references(ref_files, n_trans):
    """
    Read the reference corpus from a list of files.
    :param ref_files: List[string].
    :param n_trans: int, number of translations.
    :return: List[List[List[string]]].
    """
    references = [[] for _ in range(n_trans)]
    for file in ref_files:
        with open(file, 'r') as f:
            lines = f.read().strip().split('\n')
        assert len(lines) == n_trans, 'each reference file must have the same lines as the translation file!'
        for i, line in enumerate(lines):
            references[i].append(_break_into_words(line))
    return references


# About the format of the reference corpus.
# The current format we use for the reference corpus is multiple files where
# each provides one reference for every translation, as opposed to the previous format,
# where there is a single file containing chunks of references for each translation.
# The rational for the current format is that:
# 1. References in MT form a pool, which should be easily extended.
# 2. The number of references for each translation should be equal to one another.
# You extend or shrink the pool for all translations all together.
# You never get 2 references for trains-1 and 3 for trans-2.
# Making one set of references in one file facilitates the above rational.
# If you got a directory of references, you can run:
#
#   python bleu_metrics.py trans refs_dir/*.txt
#
# You can also control which references to include by explicitly listing them as arguments:
#
#   python bleu_metrics.py trans ref1 ref2 ref3
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("translations", help="a file storing the translations corpus, one translation per line.")
    parser.add_argument("references", nargs='+',
                        help="""One or many reference files. 
                        Line i of file j is the jth reference for ith translation. """)
    parser.add_argument("-s", "--smooth", action="store_true",
                        help="whether or not to apply smoothing (see Lin et al. 2004).")
    parser.add_argument("-n", "--ngrams", type=int, default=4, help="using n-grams up to this length.")
    args = parser.parse_args()

    with open(args.translations, 'r') as f:
        translations = [_break_into_words(line) for line in f.readlines()]

    references = _read_references(args.references, len(translations))

    # Note, Note, Note!
    # Use corpus level BLEU! Don't use sentence level and then average!
    # Corpus level is what BLEU designed to do.
    bleu_score, _, _, _ = bleu.compute_bleu(
        reference_corpus=references,
        translation_corpus=translations,
        max_order=args.ngrams,
        smooth=args.smooth,
    )

    print("BLEU: %f" % bleu_score)
