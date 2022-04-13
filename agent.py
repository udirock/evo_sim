

import numpy
from EcoEnv import EcoEnv
from MathUtils import MathUtils

class Agent:

  def __init__(self,env,baseProps=None,plasticity=None):

    self.env=env
    self.baseProps = baseProps
    if (baseProps is None):
      self.baseProps=MathUtils.genUnit(0.5,self.env.numTraits)
    #self.plasticity=plasticity
    #if (plasticity is None):
    #      self.plasticity=MathUtils.genUnif(1)[0]*0.2
    #self.phenoProps=[]
    self.fitness=None

  def grow(self):
    w = self.plasticity * 0.5
    self.phenoProps = self.baseProps * (1 - w) + self.env.target * w
    self.calc_fitness()
    self.pfit = self.fitness #MathUtils.tweakScalar(self.fitness, 0)

  def migrate(self,envs):
    if (MathUtils.bernoulli(0.1)):
      self.env=envs[numpy.random.randint(len(envs))]

  def calc_fitness(self):
    p1=self.phenoProps
    p2=self.env.target
    res=numpy.linalg.norm(p1-p2)
    self.fitness=1-res


  def spawn(self):
    ss=0.05
    nb=MathUtils.tweak(self.baseProps,ss)
    np=MathUtils.tweakScalar(self.plasticity,ss)
    res=Agent(self.env,nb,np)
    return res


  def __repr__(self):
    return f'Agent base={self.baseProps}\nfitness={self.fitness}'


  @staticmethod
  def test():
    e=EcoEnv()
    a=Agent(e)
    s=a.spawn()
    print(a)
    print(s)

    for i in range(10):
      p=i*0.1
      s1=Agent(e,s.baseProps,p)
      print("Fitness with plast",p,s1.fitness)