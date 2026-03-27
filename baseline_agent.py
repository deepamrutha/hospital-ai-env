def baseline_policy(state):
    patients = state["patients"]

    if not patients:
        return 2

    # sort by priority score (severity + wait_time)
    best_patient = max(
        patients,
        key=lambda x: (x["severity"] * 2 + x["wait_time"])
    )

    # if very critical → act immediately
    if best_patient["severity"] >= 8:
        return 0

    # if waiting too long → prioritize waiting
    if best_patient["wait_time"] > 5:
        return 1

    return 0