from src.policy import allowed

def test_rejects_other_tenant():
    assert not allowed({"tenant_id":"t2"}, {"tenant_id":"t1"})

def test_rejects_unmatched_group():
    assert not allowed({"tenant_id":"t1","allowed_groups":["finance"]},
                       {"tenant_id":"t1","groups":["engineering"]})

def test_allows_matching_group():
    assert allowed({"tenant_id":"t1","allowed_groups":["finance"]},
                   {"tenant_id":"t1","groups":["finance"]})
