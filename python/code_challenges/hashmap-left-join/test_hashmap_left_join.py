import pytest
from hashmap_left_join import left_join
from hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}
    expected = [
        ['wrath', 'anger', 'delight'],
        ['outfit', 'garb', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow'],
        ['fond', 'enamored', 'averse'],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual == expected


def test_fail():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}
    expected = [
        ['outfit', 'garb', None],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['diligent', 'employed', 'idle'],
        ['wrath', 'anger', 'delight'],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual != expected


def test_uneven_buckets():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}
    expected = [
        ['wrath', 'anger', None],
        ['outfit', 'garb', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', None],
        ['fond', 'enamored', 'averse'],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual == expected
