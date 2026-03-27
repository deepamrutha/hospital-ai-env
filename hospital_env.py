import random

class HospitalEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.max_steps = 50
        self.reset()

    # 🔄 RESET ENVIRONMENT
    def reset(self):
        self.time_step = 0

        if self.difficulty == "easy":
            self.available_beds = 5
            self.available_doctors = 3
            num_patients = 3

        elif self.difficulty == "medium":
            self.available_beds = 3
            self.available_doctors = 2
            num_patients = 6

        else:  # hard
            self.available_beds = 2
            self.available_doctors = 1
            num_patients = 10

        self.patients = [self._generate_patient() for _ in range(num_patients)]

        return self._get_state()

    # 👀 STATE
    def _get_state(self):
        return {
            "available_beds": self.available_beds,
            "available_doctors": self.available_doctors,
            "patients": self.patients,
            "time_step": self.time_step
        }

    # 🧑‍⚕️ GENERATE PATIENT
    def _generate_patient(self):
        return {
            "severity": random.randint(1, 10),
            "wait_time": 0
        }

    # 🎮 STEP FUNCTION
    def step(self, action):
        reward = 0
        treated_patient = None

        # 👉 ACTIONS
        if action == 0:  # highest severity
            if self.patients and self.available_beds > 0:
                patient = max(self.patients, key=lambda x: x["severity"])
                treated_patient = patient

        elif action == 1:  # longest waiting
            if self.patients and self.available_beds > 0:
                patient = max(self.patients, key=lambda x: x["wait_time"])
                treated_patient = patient

        elif action == 2:  # wait
            reward -= 2

        # 👉 TREAT PATIENT
        if treated_patient:
            self.patients.remove(treated_patient)
            self.available_beds -= 1

            if treated_patient["severity"] >= 8:
                reward += 10
            else:
                reward += 5

        # 👉 UPDATE WAIT TIMES
        for patient in self.patients:
            patient["wait_time"] += 1

            if patient["wait_time"] > 10:
                reward -= 5

            if patient["severity"] >= 8 and patient["wait_time"] > 5:
                reward -= 15

        # 👉 ADD NEW PATIENTS (dynamic system)
        if random.random() < 0.3:
            self.patients.append(self._generate_patient())

        # 👉 TIME UPDATE
        self.time_step += 1

        done = self.time_step >= self.max_steps

        return self._get_state(), reward, done, {}