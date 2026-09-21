from pathlib import Path
import mujoco
import mujoco.viewer
import time

# Find the XML file
xml_path = Path(__file__).parent.parent / "models" / "ball.xml"     # Instead of hardcoding paths, Path builds them safely.

# Load the model (Think of MjModel as the robot's blueprint.)
# It contains:
    # Bodies, Joints, Masses, Geometry, Gravity, Friction, Actuator
    # MjModel never changes during simulation. It's read-only.
model = mujoco.MjModel.from_xml_path(str(xml_path))




# Create simulation data
# Think of it as the robot's live state.
# MjData is the robot at this exact moment.
# It stores things like -
    # qpos -> Position
    # qvel -> Velocity
    # ctrl -> Motor commands
    # time -> Simulation Time
    # contact -> Active collisions
#This object changes every simulation step.



data = mujoco.MjData(model)

# Open a viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():


        # This is the single most important function in MuJoCo.
        # Every call performs one physics step.
        # Internally it does something like:
        # Read current position.
        # Apply gravity.
        # Detect collisions.
        # Solve Newton's equations.
        # Update velocity.
        # Update position.


        mujoco.mj_step(model, data)
        print(f"t={data.time:.3f}, z={data.qpos[2]:.3f}")

        viewer.sync()   #Draws the new state.
        time.sleep(model.opt.timestep)





# Why does MuJoCo separate MjModel and MjData instead of storing everything in one object?
# The answer relates to performance, memory reuse, and running multiple simulations from the 
# same robot model in parallel (for example, thousands of RL environments).