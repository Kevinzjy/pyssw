#!/usr/bin/env python
import os
import sys
from ssw import Aligner


def test_ssw():
    cwd = os.path.split(os.path.abspath(__file__))[0]
    with open('{}/test.fa'.format(cwd), 'r') as f:
        f.readline()
        seq1 = f.readline().rstrip()
        f.readline()
        seq2 = f.readline().rstrip()
    aligner = Aligner(str(seq1), match=1, mismatch=1, gap_open=1, gap_extend=1)
    res = aligner.align(str(seq2), 0, 19)
    sys.stderr.write(repr(res))


if __name__ == '__main__':
    test_ssw()
