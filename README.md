# BLEU
BLEU is a classical evaluation metric for machine translation based on a modified n-grams precision.

# Dependencies
- Python >= 3.6.2

# Usage

    $python bleu_metric.py [-h] [-s] [-n NGRAMS] translations references
    
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