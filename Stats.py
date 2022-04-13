

class Stats:
  def __init__(self,title):
    self.sum=0
    self.n=0
    self.sum2=0
    self.title=title

  def add(self,v):
    self.sum+=v
    self.sum2+=v*v
    self.n+=1

  def mean(self):
    if (self.n==0):
      return 0
    return self.sum/self.n

  def __repr__(self):

    return f'{self.title}: n={self.n} mean={self.mean()}'