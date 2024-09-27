#ifを使わない
import numpy as np
import time
import os
#import console
import copy
import sys
import random

w = 25
h = 15
count = 0
#count2 = 24
c = [-1,1]

def main():
  count = 0
  cells1 = np.zeros((w,h),dtype=int)
  #new_cells = np.zeros((w,h),dtype=int)
  #old_cells = np.zeros((w,h),dtype=int)
  
  def Mydef(cells1,count): 
    print(count)
    new_cells = np.copy(cells1)
    
    new_cells[23,7]=(0,1)[1< count <9]
    new_cells[22,6:10:2]=(0,1)[2< count <10]
    new_cells[21,5:10:4]=(0,1)[3< count <11]
    new_cells[20,5:10:4]=(0,1)[4< count <12]
    new_cells[19,6:10:2]=(0,1)[5< count <13]
    new_cells[20,7]=(0,1)[6< count <14]
      
    return new_cells
    
  while True:
    count += 1
    if count == 15:
      count = 1
      cells1 = np.zeros((w,h),dtype=int)
    print('Count ',count,'\n')
    
    def Loop_cells(cells1):   
      new_cells = np.copy(cells1)
      new_cells = Mydef(cells1,count)
      #最後の行に要素があれば 
      #if 0 < np.count_nonzero(new_cells[0] > 0):
        #0を代入
        #new_cells[0] = 0
      cells1 = np.copy(new_cells)	
      return cells1
  		
    def Show_cells(cells1):
      #表示
      cells5 = np.where(cells1 == 0,'  ',cells1)
      cells4 = np.where(cells1 == 1,'●',cells5)
      cells6 = np.where(cells1 == 2,'■',cells4)
      for new_cells2 in cells6:
        print(' '.join(new_cells2))
      print('\n')
      
    cells1 = Loop_cells(cells1)
    Show_cells(cells1)
    time.sleep(0.4)
    #console.clear()
    #os.system('clear')
    os.system('cls')
    
main()
