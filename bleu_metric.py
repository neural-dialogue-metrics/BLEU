import argparse
import bleu
import nltk


def _break_into_words(line):
    """
    Turn a already-tokenized line into a list of words.
    :param line: string, already tokenized. All tokens are separated by space.
    :return: List[string], broken into words.
    """
    return line.strip().split(' ')


def _read_references(file):
    """
    Read the corpus of references from a file.
    :param file: string, valid filename of line-oriented plain text.
    :return: List[List[List[string]]], the reference corpus.
    """
    with open(file, 'r') as f:
        raw_data = f.read().strip()  # Remove any leading/tailing space.
    # references for difference translations are put into chunks.
    # Within a chunk each reference lies on its own line.
    # Each chunk is separated by a blank line.
    chunks = raw_data.split('\n\n')
    references = []
    for chunk in chunks:
        references.append([_break_into_words(line) for line in chunk.strip().split('\n')])
    return references


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("translations", help="a file storing the translations corpus, one translation per line.")
    parser.add_argument("references",
                        help="""a file storing the references corpus. Multiple references for a translation
                        are put into a chunk. Within a chunk each reference lies on its own line.
                        Chunks for different translations are separated by a single blank line.
                        """)
    parser.add_argument("-s", "--smooth", action="store_true",
                        help="whether or not to apply smoothing (see Lin et al. 2004).")
    parser.add_argument("-n", "--ngrams", type=int, default=4, help="using n-grams up to this length.")
    args = parser.parse_args()

    with open(args.translations, 'r') as f:
        translations = [_break_into_words(line) for line in f.readlines()]

    references = _read_references(args.references)
    assert len(references) == len(translations), "len of translations and references should match!"

    bleu_score, *_ = bleu.compute_bleu(
        reference_corpus=references,
        translation_corpus=translations,
        max_order=args.ngrams,
        smooth=args.smooth,
    )

    # bleu_score = nltk.translate.bleu_score.corpus_bleu(references, translations)

    print("BLEU: %f" % bleu_score)
