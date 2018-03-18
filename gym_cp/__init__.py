
from gym.envs.registration import registry, register, make, spec

register(
    id='cp-v0',
    entry_point='gym_cp.envs:CpEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)
