# BLEU
BLEU is a classical evaluation metric for machine translation based on a modified n-grams precision.
It has been adopted by many dialogue researchers so it remains a baseline metric in this field.
When trying to understand a metric (not to analyse it), we mainly concern about these things:
1. What input does it takes?
2. What output does it makes?
3. How does it do that?

In the context of BLEU, we will briefly discuss these. 
1. BLEU takes a list of translations to evaluate and for each of those translation, it also takes
*one or more* references made by human experts.
It is important for you to keep in mind of the `1-to-many` relationship between the translation and the
reference.
2. BLEU outputs *a single scalar* as the score of the input. Notice that BLEU is defined upon a set of
translations and their corresponding references and it is kind of like a mean.
3. The computing process can be briefly described as:
    1. Compute the modified n-grams counts for all `n` in all translations and all their references.
    2. Compute the modified n-grams precisions based on step 1.
    3. Combine the modified n-grams precisions for all `n` into a geometric mean.
    4. Normalize the geometric mean with the brevity penalty.

## Sentence and Corpus Level BLEU
It should be pointed out that the definitions of BLEU is about 
how to compute a single scalar given *a corpus of* translations and it counts as a useful
measurement only in terms of *a corpus of* translations.

However, since a single translation _can_ make up a corpus, although it is a trivial one,
you _can_ compute a BLEU score given that, which is called *sentence level BLEU*.
Just remember however, the meaning of the sentence level BLEU is more or less a special
case of the corpus level BLEU and it is easily getting a zero value.

In [nltk](http://www.nltk.org/_modules/nltk/translate/bleu_score.html), there are two
functions corresponding to the two variants of BLEU discussed here and they are listed
for the ease of reference:
```python
def sentence_bleu(
    references,
    hypothesis,
    weights=(0.25, 0.25, 0.25, 0.25),
    smoothing_function=None,
    auto_reweigh=False,
)

def corpus_bleu(
    list_of_references,
    hypotheses,
    weights=(0.25, 0.25, 0.25, 0.25),
    smoothing_function=None,
    auto_reweigh=False,
)
```
Note `sentence_bleu()` is implemented in terms of `corpus_bleu()`.

## Rough Behavior
The default BLEU gets zero when for some `n` there is no match at all.
When this happens, the `n` that causes BLEU to be zero dominates all other `n` even if
they have reasonable values and the metric cannot give you meaningful information.

Our current implementation is that of `tensorflow/nmt`, which applies no smoothing
and retains the rough behavior. The BLEU from `nltk` however, allows various smoothing functions to be applied and even in the absence of smoothing, it filters out the zero
precision so that the final score is non-zero. In the future we may adopt this behavior
as an alternative to the default version.

# See Others
The original paper is the best resource for you to understand the algorithm.
There is a great-written entry in [Wikipedia](https://en.wikipedia.org/wiki/BLEU),
which complements the paper by working through examples and using plain language.
Also the source code of this repository and hopefully its comments will come to your aid.


# Dependencies
- Python >= 3.6.2

# Usage

   
    
where `translations` and `references` and plain text files. Each line should a sentence.
Turn on *Lin-Smoothing* by giving `-s` or `--smooth`.
The maximum length of ngrams to use is specified by `-n` or `--ngrams`.
The default value `4` is the one used as a baseline in the original paper.


# Implementation
The script `bleu.py` is adapted from `scripts/bleu.py` of 
[tensorflow/nmt](https://github.com/tensorflow/nmt.git)
with minor modification and extra comments to help understand the algorithm.


# References
[1] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
BLEU: a Method for Automatic Evaluation of Machine Translation. ACL 2002.

[2] Chin-Yew Lin, Franz Josef Och. ORANGE: a method for evaluating automatic
evaluation metrics for machine translation. COLING 2004.
