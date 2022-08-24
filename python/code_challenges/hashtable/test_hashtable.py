import pytest
from hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple_hash_value():
    hashtable = Hashtable(1024)
    actual = hashtable.hash("apple")
    expected = 854
    assert actual == expected


def test_bucket_index_is_empty():
    hashtable = Hashtable()
    actual = hashtable.set("apple", "Used for apple sauce")
    expected = [["apple", "Used for apple sauce"]]
    assert actual == expected


def test_empty_bucket_index_add_new_node():
    hashtable = Hashtable()
    actual = hashtable.set("apple", "Used for apple sauce")
    expected = [["apple", "Used for apple sauce"]]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
