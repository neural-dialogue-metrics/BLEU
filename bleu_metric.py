import argparse
import bleu

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("translations", help="a file storing translations, one per line")
    parser.add_argument("references", nargs='+',
                        help="files for one or more references, format of each is the same as translations")
    parser.add_argument("-s", "--smooth", action="store_true",
                        help="whether or not to apply smoothing (see Lin et al. 2004)")
    parser.add_argument("-n", "--ngrams", type=int, default=4, help="using n-grams up to this length")
    args = parser.parse_args()

    with open(args.translations, 'r') as f:
        translations = [line.split() for line in f.readlines()]

    references = []
    for ref in args.references:
        with open(ref, 'r') as f:
            references.append([line.split() for line in f.readlines()])

    bleu_score, *_ = bleu.compute_bleu(
        reference_corpus=references,
        translation_corpus=translations,
        max_order=args.ngrams,
        smooth=args.smooth,
    )

    print("BLEU: %f" % bleu_score)
