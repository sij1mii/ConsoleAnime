import numpy as np
import time
import os
import console
import copy
import sys
import random

w = 32
h = 15
count = 0

cells1 = np.zeros((w,h),dtype=int)
cells = np.random.randint(0,2,(1,h))
new_cells = np.zeros((w,h),dtype=int)
new_cells[0:w-1,0]=0
old_cells = np.zeros((w,h),dtype=int)

cells1[0] = cells
#cells1[0:w-1,0] = 0
c = [-1,1] #choice用配列

def Obstacle():
  #乱数で障害物作成
  r1 = random.randint(10,w-5)
  r2 = random.randint(2,h-4)
  r3 = random.randint(10,w-5)
  r4 = random.randint(2,h-4)
  r5 = random.randint(10,w-5)
  r6 = random.randint(2,h-4)
  r7 = random.randint(10,w-5)
  r8 = random.randint(2,h-4)
  r9 = random.randint(10,w-5)
  r10 = random.randint(2,h-4)
  
  return r1,r2,r3,r4,r5,r6,r7,r8,r9,r10
  
def Mydef(cells1):
   
  new_cells = np.copy(cells1)
  
  for i in range(w):
    for j in range(h):
      #●の動き
      if cells1[i,j] == 1: 
        new_cells[i,j] = 0 #自分のいるセル
        new_cells[i+1,j] = 1 #次のセル
  
        #1つ前に●
        if cells1[i+1,j] == 1:
          if cells1[i,j-1]==0 and cells1[i,j+1]==0:
            r = random.choice(c)
            if r == -1:
              new_cells[i,j]=0
              new_cells[i,j-1]=1
            elif r == 1:
              new_cells[i,j]=0
              new_cells[i,j+1]=1
  
        #1つ前に障害物
        if cells1[i+1,j] == 2:
          #両サイドに●が無ければ
          if cells1[i,j-1]==0 and cells1[i,j+1]==0:
            r = random.choice(c)#配列からランダムに選ぶ
            if r == -1: #-1なら左
              new_cells[i,j] = 0
              new_cells[i,j-1] = 1
              new_cells[i+1,j] = 2
            elif r == 1: #1なら右
              new_cells[i,j] = 0
              new_cells[i,j+1] = 1
              new_cells[i+1,j] = 2
          #左右下に障害物
          elif cells1[i,j-1]==2 and cells1[i,j+1]==1:
            new_cells[i,j] = 0
            new_cells[i-1,j-1] = 1
            new_cells[i+1,j]=2
  
          elif cells1[i,j-2]==2 and cells1[i,j+1]==1:
            new_cells[i,j] = 0
            new_cells[i-1,j+1] = 1
            new_cells[i+1,j] = 2
           
          #両サイドに障害物
          elif cells1[i,j-1]==2 and cells1[i,j+1]==2:
            r = random.choice(c)
            new_cells[i,j] = 0
            if r == -1:
              new_cells[i-1,j-1]=1
            elif r == 1:
              new_cells[i-1,j+1]=1
            new_cells[i,j-1] = 2
            new_cells[i,j+1] = 2
            new_cells[i+1,j] = 2
  
          elif cells1[i,j-2]==2 and cells1[i,j+1]==2:
            r = random.choice(c)
            new_cells[i,j] = 0
            if r == +1:
              new_cells[i-1,j+1] = 1
            elif r == -1:
              new_cells[i-1,j-1] = 1
            new_cells[i+1,j] = 2
            
          #右に●があると
          elif cells1[i,j+1] == 1:
            new_cells[i,j] = 0
            #左に跳ねる
            new_cells[i,j-1] = 1
            new_cells[i+1,j] = 2
          #右に障害物
          elif cells1[i,j+1]==2:
            new_cells[i,j] = 0
            new_cells[i,j-1] = 1
            new_cells[i,j+1] = 2
            new_cells[i+1,j] = 2
          #左に●があると
          elif cells1[i,j-1] == 1:
            new_cells[i,j] = 0
            #右に跳ねる
            new_cells[i,j+1] = 1
            new_cells[i+1,j] = 2
          #左に障害物
          elif cells1[i,j-1]==2:
            new_cells[i,j] = 0
            new_cells[i,j+1] = 1
            new_cells[i,j-1] = 2
            new_cells[i+1,j] = 2
    		
  return new_cells	

while True:
  count += 1
  #print('Count ',count,'\n')
  
  def Loop_cells(cells1):
    
    new_cells = Mydef(cells1)
    new_cells = np.copy(new_cells)

    #障害物作成
    r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 = Obstacle()
    #1行目に要素があれば
    if np.count_nonzero(new_cells[1] > 0):
      #障害物
      new_cells[r1,r2+1] = 2
      new_cells[r1+1,r2] = 2
      new_cells[r3+1,r4+1] = 2
      new_cells[r5+2,r6-1] = 2
      new_cells[r5,r6+1] = 2
      new_cells[r5-1,r6] = 2
      new_cells[r7,r8] = 2
      new_cells[r7+1,r8+2] = 2
      new_cells[r9,r10+1] = 2
      new_cells[r9+1,r10-1] = 2

    #最後の行に要素があれば 
    if np.count_nonzero(new_cells[w-1]>0):
      #0を代入
      #new_cells[0] = 0
      new_cells[w-1] = 0
    #1が無ければ
    if np.all(new_cells != 1):
      #乱数を代入
      new_cells[0] = np.random.randint(0,2,(1,h))
      new_cells[0:w-1,0]=0
      new_cells[1] = 0
      #障害物を削除
      new_cells = np.where(new_cells == 2,0,new_cells)

    cells1 = np.copy(new_cells)
    	
    return cells1
		
  def Show_cells(cells1):
    #表示
    #cells5 = np.where(cells1 == 0,'□',cells1)
    cells5 = np.where(cells1 == 0,' ',cells1)
    cells4 = np.where(cells1 == 1,'◯︎',cells5)
    cells6 = np.where(cells1 == 2,'■',cells4)
    for new_cells2 in cells6:
      print(' '.join(new_cells2))
    print('\n')
    


  cells1 = Loop_cells(cells1)
  Show_cells(cells1)
  time.sleep(0.15)
  console.clear()
  #os.system('clear')
