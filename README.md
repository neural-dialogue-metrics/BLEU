# BLEU
BLEU is a classical evaluation metric for machine translation based on a modified n-grams precision.
It has been adopted by many dialogue researchers so it remains a baseline metric in this field.
When trying to understand a metric (not to analyse it), we mainly concern about these things:
1. What input does it takes?
2. What output does it makes?
3. How does it do that?

In the context of BLEU, we will briefly discuss these. 
1. BLEU takes a list of translations to evaluate and for each of those translation, it also takes
*one or more* references, which are the so-called gold truth translations made by human experts.
It is important for you to keep in mind of the `1-to-many` relationship between the translation and the
reference.
2. BLEU outputs *a single scalar* as the score of the input. Notice that BLEU is defined upon a set of
translations and their corresponding references and it is kind of like a mean.
3. The computing process can be briefly described as:
    1. Compute the modified n-grams counts for each translation.
    2. Compute the modified n-grams precisions for each translation.
    3. Combine the modified n-grams precisions of all translation into a geometric mean.
    4. Normalize the geometric mean with the brevity penalty.
    5. That's all.

Before walking into the the details of the algorithm, let's clarify the input and output,
which defines the *signature* of the metric and helps you better understand the algorithm.

## Pitfall of I/O of BLEU
There is a model of metrics that given a set of translations and maybe other inputs, it first computes a score
for each translation *independently* and then combines each score into a final score, using some reducer
like a mean. Metrics of this model include the *Embedding-based* and *Distinct-N*.
For example, embedding-based metrics first compute how similar a single translation r.w.t a single reference
using their distributed representations and then compute their mean as the final score. 

You should note that BLEU is *not* such a model! In fact, BLEU is *not* defined on sentence level but on corpus level.
There isn't a `sentence-level BLEU` and `corpus-level BLEU`. The former is *just* a mean by some tutorial to aid your
understanding, hopefully not the opposite. Why? because when you look into its formula or source code, you can't find
such a thing that they first compute BLEU for each sentence and then somehow reduce them to a scalar.
This misunderstanding leads many people to write the wrong code or just conceptually confused.
Now you know the input of BLEU is *always* a list and a nested list for *a corpus of translation* and
*a corpus of multiple references*, respectively. And the output is always a scalar. There isn't any intermediate
BLEU for a single sentence. The single scalar is an estimation of *overall/average/general* performance of your system.
In other words, it is a kind of mean.

## Walk through the algorithm
*Fasten your seat belt as we're going to drive the point home.*

BLUE is based on *modified n-grams counts* and *modified n-grams precision*.
It does not use the counts of a single `n`, but all the counts ranging from `1` to `n`.
It first computes the above 2 statistics for each `n` (note: not for each translation).
Then it uses a geometric mean with uniform weight (which is in fact no weight) to combine the precisions of those `n`s.
Finally the BP is applied to the geometric.

# See Others
The original paper is the best resource for you to understand the algorithm.
There is a great-written entry in [Wikipedia](https://en.wikipedia.org/wiki/BLEU),
which complements the paper by working through examples and using plain language.
Also the source code of this repository and hopefully its comments will come to your aid.


# Dependencies
- Python >= 3.6.2

# Usage

    $python  bleu_metric.py [-h] [-s] [-n NGRAMS]
                      translations references [references ...]
    
where `translations` and `references` and plain text files. Each line should a sentence.
Turn on *Lin-Smoothing* by giving `-s` or `--smooth`.
The maximum length of ngrams to use is specified by `-n` or `--ngrams`.
The default value `4` is the one used as a baseline in the original paper.

# Acknowledgement
The script `bleu.py` is adapted from `scripts/bleu.py` of [tensorflow/nmt](https://github.com/tensorflow/nmt.git)
with minor modification and extra comments to help understand the algorithm.

# References
[1] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
BLEU: a Method for Automatic Evaluation of Machine Translation. ACL 2002.

[2] Chin-Yew Lin, Franz Josef Och. ORANGE: a method for evaluating automatic
evaluation metrics for machine translation. COLING 2004.