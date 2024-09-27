import numpy as np
import sys
import time
import os

class LifeGame:

  def __init__(self, L=20, rule="2 3/3"):
    self.L = L # lattice size
    p = 0.2
    self.survive = [int(i) for i in rule.split("/")[0].split()]
    self.birth = [int(i) for i in rule.split("/")[1].split()]
    lattice = np.random.random([self.L+2, self.L+2])
    self.lattice = lattice<p
    self.lattice[0,:] = self.lattice[self.L+1,:] = False
    self.lattice[:,0] = self.lattice[:,self.L+1] = False

  def canvas_update(self):
    os.system("clear")
    print ("\n")
    l = ""
    for y in range(1,self.L+1):
      for x in range(1,self.L+1):
        if self.lattice[x,y]:
        	l += u" ■"
        else:
          l += '  '
      l += "\n"
    print (l)
    print ("\n")
    time.sleep(0.3)

  def progress(self):
    L = self.L
    Tmax = 2000
    t = 0
    #while t < Tmax:
    while True:
      try:
        self.canvas_update()
        nextsites = []

        # 周期境界条件
        self.lattice[0,0] = self.lattice[self.L,self.L]
        self.lattice[0,self.L+1] = self.lattice[self.L,1]
        self.lattice[self.L+1,0] = self.lattice[1,self.L]
        self.lattice[self.L+1,self.L+1] = self.lattice[1,1]
        for m in range(1, self.L+1):
          self.lattice[m, self.L+1] = self.lattice[m, 1]
          self.lattice[m, 0] = self.lattice[m, self.L]
          self.lattice[0, m] = self.lattice[self.L, m]
          self.lattice[self.L+1, m] = self.lattice[1, m]

          # 隣接格子点の判定
        for m in range(1,self.L+1):
          for n in range(1,self.L+1):

            if self.lattice[m,n]:
              neighber = np.sum(self.lattice[m-1:m+2, n-1:n+2])-1
              if neighber in self.survive:
                  nextsites.append((m,n))
            else:
              neighber = np.sum(self.lattice[m-1:m+2, n-1:n+2])
              if neighber in self.birth:
                nextsites.append((m,n))

        # latticeの更新
        self.lattice[:] = False
        for nextsite in nextsites:
          self.lattice[nextsite] = True

        t += 1

      except KeyboardInterrupt:
        print ("stopped.")
        break

if __name__ == '__main__':

  lg = LifeGame()
  lg.progress()
