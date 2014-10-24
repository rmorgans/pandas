#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def test_to_csv_works():
    pd.DataFrame(np.random.randn(3, 100000)).to_csv('test.csv')
    assert True

def test_to_csv_doesnt_work():
    pd.DataFrame(np.random.randn(3, 100001)).to_csv('test.csv')
    assert True
