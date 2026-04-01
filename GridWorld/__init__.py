from gymnasium.envs.registration import register

register(
    id="GridWorld/GridWorld-v0",
    entry_point="GridWorld.envs:GridWorldEnv",
)
