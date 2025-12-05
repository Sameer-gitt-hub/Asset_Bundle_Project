
from src.POC_AssetBundles import functions


def test_additions():
    results = functions.add(1,1)
    assert results == 2
