import pathlib

DATA_ROOT = pathlib.Path(__file__).parent

N_TEST_REF = 3
N_TEST_TRANS = 2

TRANS_FILES = [
    DATA_ROOT / ('trans%d.txt' % i) for i in (1, 2)
]

REF_FILES = list(map(lambda i: DATA_ROOT / ('ref%d.txt' % i), (1, 2, 3)))
