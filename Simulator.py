

from agent import Agent
from EcoEnv import EcoEnv
from MathUtils import MathUtils
from Stats import Stats
import numpy

class Simulator:

  def __init__(self):
    self.numEnvs=3
    self.numAgents=10
    self.verbose=False

    ind=0
    self.envs=[]
    for i in range(self.numEnvs):
      e=EcoEnv(ind)
      ind+=1
      self.envs.append(e)



    self.agents = []
    for i in range(self.numAgents):
      self.agents.append(Agent(self.envs[i % self.numEnvs]))


  def grow(self):

    for e in self.envs:
      e.agents=[]

    for a in self.agents:
      a.migrate(self.envs)
      a.env.agents.append(a)
      a.grow()

  def next_gen(self):

    for e in self.envs:
      if (self.verbose):
        print(e.desc())
      e.assign_offsprings()

    new_agents=[]
    for e in self.envs:
      if (self.verbose):
        print("In",e.desc(),":")
      for a in e.agents:
        if (self.verbose):
          print('\tfit',a.fitness,' pfit',a.pfit,' has ',a.offsprings,'offsprings')
        for k in range(a.offsprings):
          c=a.spawn()
          new_agents.append(c)
       #   if (self.verbose):
          #print('New agent',c)

    self.agents=new_agents



  def profileGen(self):
    a_fit=0
    a_pla=0
    num_a=0
    for a in self.agents:
      a_fit+=a.fitness
      a_pla+=a.plasticity

    a_pla/=len(self.agents)
    a_fit/=len(self.agents)
    #print(f'Env {self.envs[0]}')
    print(f"Average fit {a_fit} Average plasticity {a_pla} ")
    #sa=Stats("aboveAverage")
    #sb=Stats("belowAverage")
    #for a in self.agents:
#      if (a.plasticity>a_pla):
#        sa.add(a.fitness)
#      else:
#        sb.add(a.fitness)
#    print(sa)
#    print(sb)



  def run(self):
    #self.verbose=True
    for i in range(100):
      for env in self.envs:
        env.change()
      self.grow()
      if ((i+1)%10==0):
        self.profileGen()
      agents=self.next_gen()






