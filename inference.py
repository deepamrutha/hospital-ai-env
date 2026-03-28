from hospital_env import HospitalEnv

env = HospitalEnv()

def reset():
    return env.reset()

def step(action):
    return env.step(action)