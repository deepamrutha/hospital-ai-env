from hospital_env import HospitalEnv

env = None

def reset(payload=None):
    global env

    # payload may be None OR dict
    if payload is None:
        payload = {}

    # extract difficulty safely
    level = payload.get("task_id") or payload.get("difficulty") or "easy"

    env = HospitalEnv(level)
    state = env.reset()

    return {
        "state": state
    }


def step(payload):
    global env

    if env is None:
        env = HospitalEnv("easy")
        env.reset()

    # payload expected: {"action": int}
    action = payload.get("action", 0)

    state, reward, done, info = env.step(int(action))

    return {
        "state": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }