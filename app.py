import gradio as gr
from hospital_env import HospitalEnv
from baseline_agent import baseline_policy

env = HospitalEnv("medium")
state = env.reset()

def step_env():
    global state
    action = baseline_policy(state)
    state, reward, done, _ = env.step(action)

    return f"""
State: {state}

Reward: {reward}
Done: {done}
"""

def reset_env():
    global state
    state = env.reset()
    return "Environment Reset!"

with gr.Blocks() as demo:
    gr.Markdown("# 🏥 Hospital AI Environment")

    output = gr.Textbox(label="Output")

    step_btn = gr.Button("Step")
    reset_btn = gr.Button("Reset")

    step_btn.click(step_env, outputs=output)
    reset_btn.click(reset_env, outputs=output)

demo.launch()