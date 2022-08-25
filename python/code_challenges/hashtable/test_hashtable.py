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
    assert hashtable._buckets[854] is None


def test_empty_bucket_index_add_new_node():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable._buckets[854] is not None
    assert hashtable._buckets[854].size() == 1
    assert hashtable._buckets[854].head.value == ("apple", "Used for apple sauce")


def test_bucket_index_add_new_node_to_two_different_hashes():
    hashtable = Hashtable()
    hashtable.set("bananas", "Used for banana cream pie")
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable._buckets[854] is not None
    assert hashtable._buckets[854].head.value == ("apple", "Used for apple sauce")
    assert hashtable._buckets[444].head.value == ("bananas", "Used for banana cream pie")


def test_bucket_index_with_linked_list_add_node():
    hashtable = Hashtable()
    hashtable.set("elppa", "Used for apple sauce")
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable._buckets[854].size() == 2
    assert hashtable._buckets[854].head.value == ("apple", "Used for apple sauce")


#@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_all_values_of_bucket():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("elppa", "Used for reverse apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected
    actual = hashtable.get("elppa")
    expected = "Used for reverse apple sauce"
    assert actual == expected


def test_non_existing_key():
    hashtable = Hashtable()
    actual = hashtable.get("apple")
    expected = None
    assert actual == expected


def test_return_unique_keys():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.keys()
    expected = ["listen", "silent", "ahmad"]
    assert actual == expected


def test_contains():
    hashtable = Hashtable()
    actual = hashtable.contains("apple")
    expected = False
    assert actual == expected
    hashtable.set("apple", "Used for applesauce")
    actual = hashtable.contains("apple")
    expected = True
    assert actual == expected
    hashtable.set("apple", "Used for applesauce")
    actual = hashtable.contains("banana")
    expected = False
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.to_list())

    expected = [[("listen", "to me"), ("silent", True)], [("ahmad", 30)]]

    assert actual == expected
