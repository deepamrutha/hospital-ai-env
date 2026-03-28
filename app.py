from fastapi import FastAPI
from hospital_env import HospitalEnv
from baseline_agent import baseline_policy

app = FastAPI()

# initialize env
env = HospitalEnv("medium")
state = env.reset()


@app.get("/")
def home():
    return {"message": "Hospital AI Environment Running"}


@app.post("/reset")
def reset_env():
    global state
    state = env.reset()
    return {
        "message": "Environment Reset",
        "state": state
    }


@app.post("/step")
def step_env():
    global state

    action = baseline_policy(state)
    state, reward, done, _ = env.step(action)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }