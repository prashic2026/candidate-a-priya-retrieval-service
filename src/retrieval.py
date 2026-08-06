from src.policy import allowed

def retrieve(documents, query, principal, limit=5):
    # Synthetic lexical baseline; not a production vector search implementation.
    terms = set(query.lower().split())
    eligible = [d for d in documents if allowed(d, principal)]
    ranked = sorted(eligible, key=lambda d: len(terms & set(d.get("text", "").lower().split())), reverse=True)
    return ranked[:limit]
