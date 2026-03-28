from hospital_env import HospitalEnv

env = None

def reset(payload=None):
    global env

    if payload is None:
        payload = {}

    level = payload.get("task_id") or payload.get("difficulty") or "easy"

    env = HospitalEnv(level)
    state = env.reset()

    return {
        "observation": state,
        "info": {}
    }

def step(payload):
    global env

    if env is None:
        env = HospitalEnv("easy")
        env.reset()

    action = payload.get("action", 0)

    state, reward, done, info = env.step(int(action))

    return {
        "observation": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info or {}
    }