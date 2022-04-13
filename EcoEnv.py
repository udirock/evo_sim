
import numpy
from MathUtils import MathUtils

class EcoEnv:



  def __init__(self,ind):

    self.numTraits=10
    self.target = MathUtils.genNorm(self.numTraits)
    self.target /= numpy.sum(numpy.absolute(self.target))
    #self.max_agents=10
    self.ind = ind
    self.name = chr(self.ind+65)
    #self.agents=[]


  def desc(self):
    return f'{self.ind}:{self.name}, {len(self.agents)} Agents'
    #return f'{self.ind}:{self.name}, {len(self.agents)} Agents'

  def __repr__(self):
    return f'Env target={self.target}'

  def change(self):
    self.target = MathUtils.tweak(self.target,0.05)

  def assign_offsprings(self):
    pfits = []
    for a in self.agents:
      pfits.append(a.pfit)
      a.offsprings=0

    si = numpy.flip(numpy.argsort(pfits))

    self.agents=[self.agents[i] for i in si]
    agents=self.max_agents
    i=0
    while (agents>0):
      o=1
      if (agents>self.max_agents//3):
        o=2
      self.agents[i].offsprings+=o
      agents-=o
      i=(i+1)%len(self.agents)



  num=0