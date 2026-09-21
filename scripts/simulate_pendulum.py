from pathlib import Path
import time

import mujoco
import mujoco.viewer


# -------------------------------------------------------
# Find the XML file
# Path builds the file path safely across operating systems.
# -------------------------------------------------------
xml_path = Path(__file__).parent.parent / "models" / "pendulum.xml"


# -------------------------------------------------------
# Load the model (robot blueprint)
#
# MjModel is immutable during simulation.
# It contains:
#   - Bodies
#   - Joints
#   - Geometry
#   - Masses
#   - Inertia
#   - Gravity
#   - Solver settings
# -------------------------------------------------------
model = mujoco.MjModel.from_xml_path(str(xml_path))


# -------------------------------------------------------
# Create the simulation state
#
# MjData is the live state of the robot.
# It stores:
#   qpos  -> generalized positions
#   qvel  -> generalized velocities
#   ctrl  -> actuator commands
#   time  -> simulation time
#   contact -> active contacts
# -------------------------------------------------------
data = mujoco.MjData(model)


# -------------------------------------------------------
# Initial condition (set only once)
# 0.5 rad ≈ 28.6 degrees
# -------------------------------------------------------
data.qpos[0] = 0.5
mujoco.mj_forward(model, data)


# Used to print state every 0.1 seconds
last_print = 0.0


# -------------------------------------------------------
# Open the viewer
# -------------------------------------------------------
with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():

        # Advance the simulation by one timestep
        mujoco.mj_step(model, data)

        # Print the pendulum state every 0.1 s
        if data.time - last_print >= 0.1:
            print(
                f"t={data.time:.2f} s | "
                f"qpos={data.qpos[0]:.3f} rad | "
                f"qvel={data.qvel[0]:.3f} rad/s"
            )
            last_print = data.time

        # Update the viewer
        viewer.sync()

        # Keep simulation close to real-time
        time.sleep(model.opt.timestep)


# -------------------------------------------------------
# Why separate MjModel and MjData?
#
# MjModel = Robot blueprint (shared by many simulations)
# MjData  = Current robot state (different for each simulation)
#
# This allows thousands of reinforcement learning environments
# to share one model while each has its own state.
# -------------------------------------------------------