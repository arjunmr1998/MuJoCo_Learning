# MuJoCo From Scratch

> Learning MuJoCo from first principles for Robotics, Control Systems, and Reinforcement Learning.

This repository documents my journey of understanding **MuJoCo** from the ground up instead of treating it as a black-box simulator.

Rather than jumping directly into humanoid robots, I am rebuilding the fundamentals starting with a falling ball, then a simple pendulum, and gradually moving toward robotic arms, quadrupeds, humanoids, and reinforcement learning.

The goal is to build strong intuition for **robot dynamics, control systems, and physics simulation**, which are widely used in companies like NVIDIA, Figure AI, DeepMind, Unitree, and other robotics organizations.

---

## Repository Structure

```text
MuJoCo-From-Scratch/
├── models/
│   ├── ball.xml
│   ├── pendulum.xml
│   └── mini_humanoid.xml
│
├── scripts/
│   ├── simulate_ball.py
│   ├── simulate_pendulum.py
│   └── simulate_mini_humanoid.py
│
├── notes/
├── images/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Learning Roadmap

- [x] Environment Setup
- [x] Falling Ball
- [x] Simple Pendulum
- [x] MjModel vs MjData
- [x] Generalized Coordinates (`qpos`, `qvel`)
- [ ] Two-Link Robotic Arm
- [ ] PD Controller
- [ ] Inverse Kinematics
- [ ] CartPole
- [ ] PPO from Scratch
- [ ] Humanoid Balance Controller
- [ ] Walking with Reinforcement Learning

---

# What is MuJoCo?

**MuJoCo (Multi-Joint dynamics with Contact)** is a high-performance physics engine developed by Google DeepMind for simulating robots, rigid bodies, and contact-rich interactions.

Unlike animation software, MuJoCo actually solves the equations of motion of a mechanical system.

At every simulation step it computes:

- Gravity
- Joint constraints
- Contact forces
- Accelerations
- Velocities
- Positions

using numerical integration.

This makes it widely used in:

- Robotics
- Reinforcement Learning
- Manipulation
- Humanoid Research
- Locomotion

---

# Concepts Covered

## Stage 1 – Falling Ball

**Files**

- `models/ball.xml`
- `scripts/simulate_ball.py`

### Concepts Learned

- MJCF (MuJoCo XML Format)
- World Coordinates
- Gravity
- Free Joints
- `MjModel`
- `MjData`
- Simulation Loop
- `mj_step()`

---

## Stage 2 – Simple Pendulum

**Files**

- `models/pendulum.xml`
- `scripts/simulate_pendulum.py`

### Concepts Learned

- Hinge Joints
- Degrees of Freedom (DOF)
- `qpos`
- `qvel`
- Generalized Coordinates
- Parent-Child Body Hierarchy
- Joint Axis
- Contact Constraints

---

## Stage 3 – Mini Humanoid

**Files**

- `models/mini_humanoid.xml`
- `scripts/simulate_mini_humanoid.py`

### Concepts Learned

- Kinematic Trees
- Floating Base
- Multiple Joints
- Hierarchical Bodies

---

# Installation (Windows)

This repository was developed on:

- Windows 11
- Python 3.12
- MuJoCo 3.x

## Step 1 – Install Python

Download Python 3.12 (or newer).

**Official website**

https://www.python.org/downloads/

Verify installation:

```bash
py -0p
```

Example output:

```text
-V:3.12    C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe
```

---

## Step 2 – Download MuJoCo

Although the Python package includes MuJoCo, you can also explore the official project.

- GitHub: https://github.com/google-deepmind/mujoco
- Documentation: https://mujoco.readthedocs.io/

---

## Step 3 – Clone the Repository

```bash
git clone https://github.com/------
cd MuJoCo-From-Scratch
```

---

## Step 4 – Create a Virtual Environment

```bash
py -3.12 -m venv .venv
```

Activate it.

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If execution is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

You should now see:

```text
(.venv) PS C:\Users\YourName\MuJoCo-From-Scratch>
```

---

## Step 5 – Install Dependencies

```bash
pip install -r requirements.txt
```

Generate `requirements.txt` using:

```bash
pip freeze > requirements.txt
```

Typical packages include:

```text
mujoco==3.x.x
numpy
glfw
```

---

## Step 6 – Verify Installation

```bash
python -c "import mujoco; print(mujoco.__version__)"
```

Example:

```text
3.3.0
```

---

# Running Simulations

## Falling Ball

```bash
python scripts/simulate_ball.py
```

---

## Pendulum

```bash
python scripts/simulate_pendulum.py
```

---

## Mini Humanoid

```bash
python scripts/simulate_mini_humanoid.py
```

---

# Understanding the Code

Every simulation follows the same structure.

```python
model = mujoco.MjModel.from_xml_path("model.xml")
data = mujoco.MjData(model)

while running:
    mujoco.mj_step(model, data)
```

The workflow looks like this.

```text
XML
 ↓
MjModel (Blueprint)
 ↓
MjData (Live State)
 ↓
mj_step()
 ↓
Viewer
```

---

## MjModel

Think of `MjModel` as the robot's **blueprint**.

It stores:

- Bodies
- Joints
- Geometry
- Mass
- Inertia
- Gravity
- Solver Settings

It does **not** change during simulation.

---

## MjData

`MjData` is the robot's **live state**.

It stores:

- `qpos` (Generalized Positions)
- `qvel` (Generalized Velocities)
- `ctrl` (Motor Commands)
- `time` (Simulation Time)
- Contact Information

This object changes every call to `mj_step()`.

---

# Why Use a Virtual Environment?

The `.venv` folder creates an isolated Python environment for this project.

This prevents dependency conflicts with other Python projects.

The `.venv` folder is intentionally **not committed** to GitHub because anyone can recreate it using:

```bash
py -3.12 -m venv .venv
pip install -r requirements.txt
```

---

# MuJoCo Viewer Controls

Useful controls while running a simulation.

| Action | Control |
|---------|---------|
| Pause / Resume | `Space` |
| Rotate Camera | Right Mouse Drag |
| Pan Camera | Middle Mouse Drag |
| Zoom | Mouse Scroll |

---



# Future Goals

Planned additions include:

- Two-Link Manipulator
- Forward Kinematics
- Inverse Kinematics
- PD Controller
- CartPole
- Hopper
- Quadruped
- Humanoid Balancing
- PPO Implementation from Scratch
- Sim-to-Real Concepts

---

# Official Resources

- MuJoCo GitHub Repository: https://github.com/google-deepmind/mujoco
- MuJoCo Documentation: https://mujoco.readthedocs.io/
- Python Downloads: https://www.python.org/downloads/

---

# License

This repository is intended for educational purposes and personal learning.

The simulation code in this repository is written as original learning examples, while MuJoCo itself is an open-source project maintained by Google DeepMind.