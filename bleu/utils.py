# MIT License
# 
# Copyright (c) 2019 Cong Feng.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__all__ = [
    "load_reference_corpus",
    "load_translation_corpus",
]


def load_reference_corpus(files):
    references = None
    for file in files:
        with open(file) as f:
            lines = f.read().strip().split("\n")
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
