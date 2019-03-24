import os
from bleu.utils import load_translation_corpus, load_reference_corpus

DATA_ROOT = os.path.join(os.path.dirname(__file__), 'data')

assert os.path.isdir(DATA_ROOT)

# Load the small data right here.
reference_corpus = load_reference_corpus(
    [os.path.join(DATA_ROOT, 'ref%d.txt' % i) for i in range(1, 4)]
)

translation_corpus = [
    load_translation_corpus(os.path.join(DATA_ROOT, 'trains%d.txt' % i))
    for i in range(1, 3)
]

if __name__ == '__main__':
    from pprint import pprint

    pprint(reference_corpus)
    pprint(translation_corpus)
