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
from pathlib import Path

from bleu import *
from bleu.utils import load_reference_corpus
from bleu.utils import load_translation_corpus
from agenda.metric_helper import write_score


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


def eval_metric(translations, references, n, type, output_dir):
    name = 'bleu_%d' % n
    output_dir = Path(output_dir)
    output = output_dir.joinpath(name).with_suffix('.json')

    scores = [
        getattr(bleu_sentence_level(trans, ref, max_order=n, smooth=True), type)
        for trans, ref in zip(translations, references)
    ]

    system = getattr(bleu_corpus_level(
        translation_corpus=translations,
        reference_corpus=references,
        max_order=n,
        smooth=True,
    ), type)

    write_score(
        name=name,
        scores=scores,
        system=system,
        output=output,
        params={
            'type': type,
            'n': n,
            'smooth': True,
        }
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', "-translations")
    parser.add_argument('-r', "-references", nargs='+')
    parser.add_argument("-n", "--n_grams", nargs='+', type=int)
    parser.add_argument('--type', choices=('bleu', 'geo_mean', 'precisions'), default='bleu')
    parser.add_argument('--output_dir')
    args = parser.parse_args()

    translations = load_translation_corpus(args.translations)
    references = load_reference_corpus(args.references)

    for n in args.n_grams:
        eval_metric(
            translations=translations,
            references=references,
            n=n,
            type=args.type,
            output_dir=args.output_dir,
        )
