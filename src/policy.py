def allowed(document, principal):
    if document.get("tenant_id") != principal.get("tenant_id"):
        return False
    allowed_groups = set(document.get("allowed_groups", []))
    principal_groups = set(principal.get("groups", []))
    return not allowed_groups or bool(allowed_groups & principal_groups)
