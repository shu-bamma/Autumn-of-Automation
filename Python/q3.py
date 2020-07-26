class Complex:
  def __init__(self,r,i):  #The constructor
    self.r=r
    self.i=i
  def display(self):
    if self.i>0:
      print(str(self.r)+'+'+str(self.i)+'i')
    elif self.i==0:
      print(str(self.r))
    else:
      print(str(self.r)+'-'+str(abs(self.i))+'i')

  def modulus(self):
    mod=self.i**2+self.r**2
    return mod

  def conjugate(self):
    c=Complex(0,0)
    c.i=self.i*-1
    c.r=self.r
    return c
  
  def add(self,a):
    c=Complex(0,0)
    c.r=self.r+a.r
    c.i=self.i+a.i
    return c
  def sub(self,a):
    c=Complex(0,0)
    c.r=self.r-a.r
    c.i=self.i-a.i
    return c
  def mul(self,a):
    c=Complex(0,0)
    c.r=(self.r*a.r)-(self.i*a.i)
    c.i=(self.r*a.i)+(self.i*a.r)
    return c
  
  def inv(self):
    c=Complex(0,0)
    con=self.conjugate()
    c.r=con.r/(self.modulus())
    c.i=con.i/(self.modulus())
    return c