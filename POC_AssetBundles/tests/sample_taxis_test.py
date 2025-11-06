
from src.POC_AssetBundles import functions


def test_additions():
    results = taxis.add(1,1)
    assert results.count() == 5
