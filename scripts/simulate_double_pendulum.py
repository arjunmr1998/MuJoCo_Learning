from pathlib import Path
import time

import mujoco
import mujoco.viewer

xml_path = Path(__file__).parent.parent / "models" / "double_pendulum.xml"

model = mujoco.MjModel.from_xml_path(str(xml_path))
data = mujoco.MjData(model)

# Initial angles (radians)
data.qpos[0] = 0.6   # Shoulder
data.qpos[1] = -0.3  # Elbow

# Recompute body positions after changing qpos
mujoco.mj_forward(model, data)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():

        mujoco.mj_step(model, data)

        viewer.sync()
        time.sleep(model.opt.timestep)