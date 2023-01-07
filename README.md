# A BLEU Implementation

## User Guide

This guide will get you started using our BLEU metric.

### Use-case 1: I have my data in files.

Machine translation system output things to files. Your gold reference resides in files. It is thus a common case to run the evaluation based on files. If you just want to do an evaluation and see the result, the command line tool will get you right.
```bash
# Put your translation corpus in trans.txt.
# Put your reference corpus in another file, say ref.txt.
# If you have multiple references, just put them in more files, like r1.txt, r2.txt...
# Run this command, use -s to turn on smoothing:
bleu_metric.py trans.txt ref.txt

# The output will look like:
BLEU: 0.023333
```

### Use-case 2: I have my data in files, but want to use it programmatically.

You can load your data files with our helper functions:
```python
import bleu

# Note: the builder functions return things in *corpus* format. 
trans = bleu.load_translation_corpus('your_file')
refs = bleu.load_reference_corpus(['file_1', 'file_2', 'file_3'])

# Data is suitable for corpus level evaluation.
score = bleu.bleu_corpus_level(trans, refs, max_order=2)

```

### Use-case 3: My data is generated programmatically.

You can just pass your data to the metric functions. You need to ensure your data is in the right shape (either corpus or sentence) as expected by the functions.
```python
import bleu

# If you have a translation and reference corpus:
score = bleu.bleu_corpus_level(
    translation_corpus=[
        'sentence 1'.split(),
        'sentence 2'.split(),
    ],
    reference_corpus=[
        [
            'reference 1 for sentence 1'.split(),
            'reference 2 for sentence 1'.split(),
        ],
        [
            'reference 1 for sentence 2'.split(),
            'reference 2 for sentence 2'.split(),
        ]
    ]
)

print(score)

# Or if you have a translation sentence:
score = bleu.bleu_sentence_level(
    translation_sentence='sentence 1'.split(),
    reference_corpus=[
        'reference 1 for sentence 1'.split(),
        'reference 2 for sentence 1'.split(),
    ]
)

```
Note that every single sentence must be a list of strings.

## Installation

### Dependencies

- Python >= 3.6.2

### Install

```bash
git clone https://github.com/neural-dialogue-metrics/BLEU.git
cd BLEU
pip install -e .
```

## Introduction to BLEU

BLEU is a classical evaluation metric for machine translation based on a modified n-grams precision. It has been adopted by many dialogue researchers so it remains a baseline metric in this field. When trying to understand a metric, we are mainly concerned about these things:

1. What input does it take?
2. What output does it make?
3. How does it do that?

In the context of BLEU, we will briefly discuss these. 

1. BLEU takes a list of translations to evaluate and for each of those translations, it takes *one or more* references made by human experts.
You need to keep in mind the `1-to-many`` relationship between the translation and the reference.
2. BLEU outputs *a single scalar* as the score of the input. Notice that BLEU is defined upon a set of translations and their corresponding references and it is kind of like a mean.
3. The computing process can be briefly described as:
    1. Compute the modified n-gram counts for all `n` in all translations and all their references.
    2. Compute the modified n-gram precisions based on step 1.
    3. Combine the modified n-gram precisions for all `n` into a geometric mean.
    4. Normalize the geometric mean with the brevity penalty.

### Sentence and Corpus Level BLEU

It should be pointed out that the definition of BLEU is about how to compute a single scalar given *a corpus of* translations and it counts as a useful measurement only in terms of *a corpus of* translations.

However, since a single translation _can_ make up a corpus, although it is a trivial one, you _can_ compute a BLEU score given that, which is called *sentence level BLEU*. Just remember, however, the meaning of the sentence level BLEU is more or less a special case of the corpus level BLEU and it is easily getting a zero value without smoothing.

In [nltk](http://www.nltk.org/_modules/nltk/translate/bleu_score.html), there are two functions corresponding to the two variants of BLEU discussed here and they are listed for ease of reference:

```python
nltk.translate.bleu_score.sentence_bleu
nltk.translate.bleu_score.corpus_bleu
```

Note that `sentence_bleu()` is implemented in terms of `corpus_bleu()`.

### Rough Behavior

The default BLEU gets zero when for some `n` there is no match at all. When this happens, the `n` that causes BLEU to be zero dominates all other `n` even if they have reasonable values and the metric cannot give you meaningful information.

Our current implementation is that of `tensorflow/nmt`, which applies no smoothing by default. It implements the smoothing technique from [2] and you can pass `smooth=True` to `compute_blue` or `-s` to the `bleu_metric.py`.

As a side note, the BLEU from `nltk` allows various smoothing functions to be applied, and even in the absence of smoothing, it filters out the zero precision so that the final score is non-zero. In the future, we may adopt this behavior as an alternative to the default version.

### See Also

The original paper is the best resource for you to understand the algorithm. There is a great-written entry in [Wikipedia](https://en.wikipedia.org/wiki/BLEU), which complements the paper by working through examples and using plain language. Also, the source code of this repository and hopefully its comments will come to your aid.

## Examples

To run the metric over a translation corpus and a reference corpus, run the following command:
```bash
$ python bleu_metric.py translation ref1 ref2 ...
```
We prepare two examples in the folder `testdata/` from the original paper. They are two candidate translations and three reference translations.

Candidates:

    It is to insure the troops forever hear the activity guidebook that the party directs.
    It is a guide to action that ensures that the military always obeys the commands of the party.

References:
    
    It is a guide to action that ensures that the military will forever heed Party commands.
    It is the guiding principle that guarantees the military forces always being under the command of the Party.
    It is the practical guide for the army always to heed the directions of the party.
   
To see the score for each candidate, you can run the following commands:

    cd testdata
    python ../bleu_metric.py ./trans1.txt ./ref1.txt ./ref2.txt ./ref3.txt -s
    BLEU: 0.128021
    
    python ../bleu_metric.py ./trans2.txt ./ref1.txt ./ref2.txt ./ref3.txt -s
    BLEU: 0.570435
  
You can see that score for the `trans2.txt` is higher than that of `trans1.txt`, matching the result of the original paper.

Note that since our translation corpus is a trivial one that only contains one sentence, we pass the `-s` option to avoid rough behavior.

The meanings of the positional and optional arguments are straightforward. One can pass the `-h` option to find out.


## Acknowledgment

The script `bleu.py` is adapted from `scripts/bleu.py` of [tensorflow/nmt](https://github.com/tensorflow/nmt.git) with minor modifications and extra comments to help understand the algorithm.


## Reference

[1] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. BLEU: a Method for Automatic Evaluation of Machine Translation. ACL 2002.

[2] Chin-Yew Lin, Franz Josef Och. ORANGE: a method for evaluating automatic evaluation metrics for machine translation. COLING 2004.
