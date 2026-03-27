# 🏥 Hospital Resource Allocation AI Environment

## 📌 Problem
Hospitals face challenges in managing limited resources like beds and doctors while handling patients with varying severity levels.

## 🎯 Solution
We built an AI environment where an agent learns how to allocate resources efficiently using reinforcement learning principles.

## ⚙️ Environment Design

### State
- Available beds
- Available doctors
- Patient list (severity, wait time)
- Time step

### Actions
- Assign highest severity patient
- Assign longest waiting patient
- Wait

### Reward
- +10 for critical patients
- +5 for normal patients
- -15 for ignoring critical patients
- -5 for long waiting
- -2 for idle

## 🧪 Tasks
- Easy → fewer patients
- Medium → balanced
- Hard → high load

## ▶️ Run

```bash
python run.py