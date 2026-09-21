from pathlib import Path
import time

import mujoco
import mujoco.viewer

# ----------------------------------------------------
# Load the Mini Humanoid model
# ----------------------------------------------------
xml_path = Path(__file__).parent.parent / "models" / "mini_humonid.xml"

model = mujoco.MjModel.from_xml_path(str(xml_path))
data = mujoco.MjData(model)

# ----------------------------------------------------
# Give the humanoid a slight forward lean.
# (We'll learn why this is useful later.)
# ----------------------------------------------------
data.qpos[4] = 0.1     # Small torso rotation
mujoco.mj_forward(model, data)

last_print = 0

# ----------------------------------------------------
# Launch viewer
# ----------------------------------------------------
with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():

        mujoco.mj_step(model, data)

        if data.time - last_print >= 0.2:
            print(
                f"Time: {data.time:.2f}s | "
                f"Bodies: {model.nbody} | "
                f"Joints: {model.njnt} | "
                f"DOFs: {model.nv}"
            )
            last_print = data.time

        viewer.sync()
        time.sleep(model.opt.timestep)