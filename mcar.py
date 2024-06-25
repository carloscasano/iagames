import gym
env = gym.make('MountainCar-v0')

env.reset()
final = False
while not final:
    accion = 0
    nuevo_estado, recompensa , final, info = env.step(accion)
    env.render()
env.close()
