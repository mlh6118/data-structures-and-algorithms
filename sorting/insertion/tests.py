import pytest
from insertion_sort import insertion_sort


def test_insertion_sort_exists():
    assert insertion_sort


def test_insertion_sort(array_to_sort):
    actual = insertion_sort(array_to_sort)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_empty_array():
    actual = insertion_sort([])
    expected = []
    assert actual == expected


def test_already_sorted():
    actual = insertion_sort([4, 8, 15, 16, 23, 42])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_perfectly_backwards():
    actual = insertion_sort([42, 23, 16, 15, 8, 4])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


@pytest.fixture
def array_to_sort():
    arr = [8, 4, 23, 42, 16, 15]
    return arr
