def verification_score(info):

    score = 0

    if info.get("website"):
        score += 30

    if info.get("phone"):
        score += 35

    if info.get("email"):
        score += 35

    return score