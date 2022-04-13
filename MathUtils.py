
import numpy

class MathUtils:

  @staticmethod
  def genUnif(n):
    res=numpy.random.uniform(0,1,n)
    return res

  @staticmethod
  def genUnifScalar(n):
    return self.genUnif(n)[0]

  @staticmethod
  def bernoulli(p):
    return numpy.random.binomial(1, p) > 0


  @staticmethod
  def tweak(vec,std):
    res=vec + numpy.random.normal(0, std, len(vec))
    res = numpy.minimum(res, 1)
    res=numpy.maximum(res,0)
    return res

  @staticmethod
  def tweakScalar(vec, std):
    res = vec + numpy.random.normal(0, std, 1)[0]
    res = numpy.minimum(res, 1)
    res = numpy.maximum(res, 0)
    return res

  @staticmethod
  def test():
    print('random unif data')
    for i in range(3):
       u1=MathUtils.genUnif(3)
       print(u1)
    print('last row tweaked with 0.01')
    for i in range(3):
      print(MathUtils.tweak(u1,0.01))
    print('last row tweaked with 0.1')
    for i in range(3):
      print(MathUtils.tweak(u1, 0.1))
    print('last row tweaked with 1')
    for i in range(3):
      print(MathUtils.tweak(u1, 1))
    print('scalar 0.2 tweaked with 0.2')
    for i in range(10):
      print(MathUtils.tweakScalar(0.2, 0.2))


