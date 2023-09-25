from typing import Optional

import gymnasium as gym

def make_env(full_env_name, cfg=None, env_config=None, render_mode: Optional[str] = None):
    return gym.make(full_env_name, render_mode=render_mode)