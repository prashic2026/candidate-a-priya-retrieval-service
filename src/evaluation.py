def recall_at_k(relevant_ids, retrieved_ids, k=5):
    relevant = set(relevant_ids)
    if not relevant:
        return 0.0
    return len(relevant & set(retrieved_ids[:k])) / len(relevant)
