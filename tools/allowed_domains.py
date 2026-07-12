def is_allowed(target: str) -> bool:
    with open("allowed_domains.txt") as f:
        allowed = [line.strip() for line in f if line.strip()]
    return target in allowed