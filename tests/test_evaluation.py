from src.evaluation import recall_at_k

def test_recall_at_k():
    assert recall_at_k(["a","b"], ["a","x","b"], 3) == 1.0

def test_empty_relevance():
    assert recall_at_k([], ["a"], 5) == 0.0
