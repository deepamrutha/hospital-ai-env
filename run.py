from hospital_env import HospitalEnv
from baseline_agent import baseline_policy
from grader import grade   # 👈 ADD THIS

def run_episode(difficulty):
    env = HospitalEnv(difficulty)
    state = env.reset()
    total_reward = 0

    done = False

    while not done:
        action = baseline_policy(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        score = run_episode(level)
        normalized = grade(score)   # 👈 ADD THIS

        print(f"{level.upper()} SCORE: {score}")
        print(f"{level.upper()} GRADE: {normalized}")