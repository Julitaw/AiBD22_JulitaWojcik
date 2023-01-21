import pytest
from app import main
import numpy as np
testdata = [
    ([7,5,3,2,9,8,10],([2, 3, 5, 7, 8, 9, 10], 18)),
    ([6,4,9,1,8,50,45,7,8,34,78,23,6,7,90,1000],([1, 4, 6, 6, 7, 7, 8, 8, 9, 23, 34, 45, 50, 78, 90, 1000], 105)),
    ('kasia', None)
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_bubblesort(sample, expected_output):
    assert main.bubblesort(sample) == expected_output