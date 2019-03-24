__all__ = [
    "load_reference_corpus",
    "load_translation_corpus",
]


def load_reference_corpus(files):
    references = None
    for file in files:
        with open(file) as f:
            lines = f.read().strip().split('\n')
        if not references:
            references = [[] for _ in range(len(lines))]
        else:
            # 'each reference file must have the same lines as the translation file!'
            assert len(lines) == len(references)
        for i, line in enumerate(lines):
            references[i].append(line.split())
    return references


def load_translation_corpus(file):
    with open(file) as f:
        return [line.split() for line in f.readlines()]
