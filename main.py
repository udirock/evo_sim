

from agent import Agent
from EcoEnv import EcoEnv
from MathUtils import MathUtils
from Simulator import Simulator

print("Starting")

e=EcoEnv(0);
a=Agent(e)
print(e)
print(a)


# Plan:
# a Have one environment
#   Trait*envTrait add up to form fitness
#   Compare prob vs. Fisher eq.
# b Have two environments
#   Each agent chooses best fitting one
#   Compare prob vs. Fisher eq.
# c Add p trait
#   Only works with first env
#   Compare prob vs. Fisher eq.

#MathUtils.test()
#Agent.test()

#s=Simulator()
#s.run()


# Todos add migration, add better fitness if few fill an eco