#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def test_to_csv():
    import gzip
    f = gzip.open('to_csv_test.msgpack.gz', 'rb')
    d=pd.read_msgpack(f)
    d.to_csv('test.csv')
    assert True
