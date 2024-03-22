import  numpy as np
#import console
import os
import random
import time
import sys

#探索様子を追跡する関数（迷路の更新を出力する）
def track(maze,start,depth):
  draw = str(depth)+'\n'
  
  for x in range(25):
    for y in range(18):
      if maze[x,y] == 9:
        draw += "■ "    #壁
      elif maze[x,y] == 2:
        draw += "* "    #探索済みの道
        #draw += '  '
      elif maze[x,y] == 3:
        draw += '〇'#現在地
      else:
        draw += "  "    #未探索
    draw += "\n"
  print(draw)
  
def Maze2(start):

  global direction
  global r_direction 
  
  pos = start.copy()
  #print('pos1',pos)
  pos_old = pos 

  while True:
    #print('pos2',pos)  
    x,y,depth = pos.pop()

    #print('pos',x,y,depth)
    #print('depth',depth)

    #現在地
    maze[x,y] = 3   
    #コンソール表示  
    #print(maze)
    
    #1秒ごとに図の更新
    time.sleep(0.05)
    os.system('cls')
    #console.clear()
    track(maze,start,depth)
    print('d',depth)
    
    
    #maze_nowに現在地を入れてmazeに実行済みを入れる
    maze_now = maze
    if maze_now[x,y] == 3:
      maze[x,y] = 2

    #条件設定
    #パターン1  
    if maze[x-1,y] == 9 and maze[x,y-1] == 0 and maze[x,y+1] == 0:
      r_direction = random.choice(direction)
      print('p1r:',r_direction)
      if r_direction == 1 or r_direction == 2:#左下
        pos.append([x+1,y-1,depth+1])
        if maze[x+1,y-1] == 2:
          maze[x+1,y-1] = 0
      if r_direction == 3:#下
        pos.append([x+1,y,depth+1])
      if r_direction == 4 or r_direction == 5:#右下
        pos.append([x+1,y+1,depth+1])
        if maze[x+1,y+1] == 2:
          maze[x+1,y+1] = 0
        
    #パターン2
    if maze[x,y-1] == 9 and maze[x-1,y] == 0 and maze[x+1,y] == 0:
      #maze[2:-2,2:-2] = 0
      r_direction = random.choice(direction)
      print('p2r:',r_direction)
      if maze[x,y+1] == 2:
        maze[x,y+1] = 0
        if r_direction == 1:#上        
          pos.append([x-1,y,depth+1])
        if r_direction == 2:#右上
          pos.append([x-1,y+1,depth+1])
        if r_direction == 3:#右
          pos.append([x,y+1,depth+1])
        if r_direction == 4:#右下
          pos.append([x+1,y+1,depth+1])
        if r_direction == 5:#下
          pos.append([x+1,y,depth+1])
      if maze[x-1,y+1] == 2:
        maze[x-1,y+1] = 0
        if r_direction == 2:#右上
          pos.append([x-1,y+1,depth+1])
        if r_direction == 3:#右
          pos.append([x,y+1,depth+1])
        if r_direction == 1 or 4:#右下
          pos.append([x+1,y+1,depth+1])
        if r_direction == 5:#下
          pos.append([x+1,y,depth+1])
      if maze[x+1,y+1] == 2:
        maze[x+1,y+1] = 0
        if r_direction == 2 or 5:#右上
          pos.append([x-1,y+1,depth+1])
        if r_direction == 3:#右
          pos.append([x,y+1,depth+1])
        if r_direction == 1 or 4:#右下
          pos.append([x+1,y+1,depth+1])

    #パターン3
    if maze[x,y+1] == 9 and maze[x-1,y] == 0 and maze[x+1,y] == 0:
      #maze[2:-2,2:-2] = 0
      r_direction = random.choice(direction)
      print('p3r:',r_direction)
      if maze[x,y-1] == 2:
        maze[x,y-1] = 0
        if r_direction == 1:#上        
          pos.append([x-1,y,depth+1])
        if r_direction == 2:#左上
          pos.append([x-1,y-1,depth+1])
        if r_direction == 3:#左
          pos.append([x,y-1,depth+1])
        if r_direction == 4:#左下
          pos.append([x+1,y-1,depth+1])
        if r_direction == 5:#下
          pos.append([x+1,y,depth+1])
      if maze[x-1,y-1] == 2:
        maze[x-1,y-1] = 0
        if r_direction == 2:#左上
          pos.append([x-1,y-1,depth+1])
        if r_direction == 3:#左
          pos.append([x,y-1,depth+1])
        if r_direction == 1 or 4:#左下
          pos.append([x+1,y-1,depth+1])
        if r_direction == 5:#下
          pos.append([x+1,y,depth+1])
      if maze[x+1,y-1] == 2:
        maze[x+1,y-1] = 0
        if r_direction == 1:#上        
          pos.append([x-1,y,depth+1])
        if r_direction == 2 or 5:#左上
          pos.append([x-1,y-1,depth+1])
        if r_direction == 3:#左
          pos.append([x,y-1,depth+1])
        if r_direction == 4:#左下
          pos.append([x+1,y-1,depth+1])

    #パターン4
    if maze[x+1,y] == 9 and maze[x,y-1] == 0 and maze[x,y+1] == 0:
      maze[2:-2,2:-2] = 0
      r_direction = random.choice(direction)
      print('p4r:',r_direction)
      if r_direction == 1:#左        
        pos.append([x,y-1,depth+1])
      if r_direction == 2:#左上
        pos.append([x-1,y-1,depth+1])
      if r_direction == 3:#上
        pos.append([x-1,y,depth+1])
      if r_direction == 4:#右上
        pos.append([x-1,y+1,depth+1])
      if r_direction == 5:#右
        pos.append([x,y+1,depth+1])
        
        
    #パターン5
    if maze[x,y+1] == 9 and maze[x,y-1] == 2 and maze[x+1,y] == 9:#下壁
      maze[x,y-1] = 0
      r_direction = random.choice(direction)
      print('p5r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x-1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y-1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x-1,y-1,depth+1])
        
    #パターン6
    if maze[x,y-1] == 9 and maze[x,y+1] == 2 and maze[x+1,y] == 9:#下壁
      maze[x,y+1] = 0
      r_direction = random.choice(direction)
      print('p6r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x-1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y+1,depth])
      if r_direction == 2 or 4:
        pos.append([x-1,y+1,depth+1])
        
    #パターン7
    if maze[x,y+1] == 9 and maze[x,y-1] == 2 and maze[x-1,y] == 9:#上壁
      maze[x,y-1] = 0
      r_direction = random.choice(direction)
      print('p7r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x+1,y,depth+1])
      if r_direction == 2 or 4:
        pos.append([x+1,y-1,depth+1])
        
    #パターン8
    if maze[x,y-1] == 9 and maze[x,y+1] == 2 and maze[x-1,y] == 9:#上壁
      maze[x,y+1] = 0
      r_direction = random.choice(direction)
      print('p8r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x+1,y,depth+1])
      if r_direction == 2 or 4:
        pos.append([x+1,y+1,depth+1])
        
    #パターン9
    if maze[x,y+1] == 9 and maze[x-1,y] == 2 and maze[x+1,y] == 9:#下壁
      maze[x-1,y] = 0
      r_direction = random.choice(direction)
      print('p9r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x-1,y-1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y-1,depth+1])
        
    #パターン10
    if maze[x,y-1] == 9 and maze[x-1,y] == 2 and maze[x+1,y] == 9:#下壁
      maze[x-1,y] = 0
      r_direction = random.choice(direction)
      print('p10r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x-1,y+1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y+1,depth+1])
        
    #パターン11   
    if maze[x,y-1] == 9 and maze[x-1,y+1] == 2 and maze[x-1,y-1] == 9:#下壁
      maze[x-1,y+1] = 0
      r_direction = random.choice(direction)
      print('p11r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x-1,y,depth+1])
      if r_direction == 5:
        pos.append([x-1,y+1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y+1,depth+1])
        
    #パターン12
    if maze[x,y+1] == 9 and maze[x-1,y-1] == 2 and maze[x+1,y] == 9:#下壁
      maze[x-1,y-1] = 0
      r_direction = random.choice(direction)
      print('p12r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x-1,y,depth+1])
      if r_direction == 5:
        pos.append([x-1,y-1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y-1,depth+1])
        
    #パターン13
    if maze[x,y+1] == 9 and maze[x+1,y] == 2 and maze[x-1,y] == 9:#上壁
      maze[x+1,y] = 0
      r_direction = random.choice(direction)
      print('p13r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x+1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y-1])
      if r_direction == 2 or 4:
        pos.append([x+1,y-1,depth+1])
        
    #パターン14
    if maze[x,y-1] == 9 and maze[x+1,y] == 2 and maze[x-1,y] == 9:#上壁
      maze[x+1,y] = 0
      r_direction = random.choice(direction)
      print('p14r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x+1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y+1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x+1,y+1,depth+1])
        
    #パターン15
    if maze[x,y+1] == 9 and maze[x,y-1] == 2 and maze[x+1,y] == 9:#下壁
      maze[x,y-1] = 0
      r_direction = random.choice(direction)
      print('p9r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x-1,y-1,depth+1])
      if r_direction == 5:
        pos.append([x-1,y,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y-1,depth+1])
        
    #パターン16
    if maze[x,y-1] == 9 and maze[x,y+1] == 2 and maze[x+1,y] == 9:#下壁
      maze[x,y+1] = 0
      r_direction = random.choice(direction)
      print('p10r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x-1,y+1,depth+1])
      if r_direction == 5:
        pos.append([x-1,y,depth+1])
      if r_direction == 2 or 4:
        pos.append([x,y+1,depth+1])

    #パターン17
    if maze[x,y+1] == 9 and maze[x+1,y-1] == 2 and maze[x-1,y] == 9:#上壁
      maze[x+1,y-1] = 0
      r_direction = random.choice(direction)
      print('p13r:',r_direction)
      if r_direction == 1 or 3:
        pos.append([x+1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y-1])
      if r_direction == 2 or 4:
        pos.append([x+1,y-1,depth+1])
        
    #パターン18
    if maze[x,y-1] == 9 and maze[x+1,y+1] == 2 and maze[x-1,y] == 9:#上壁
      maze[x+1,y+1] = 0
      r_direction = random.choice(direction)
      print('p14r:',r_direction)
      if r_direction == 1 or 3 or 5:
        pos.append([x+1,y,depth+1])
      if r_direction == 5:
        pos.append([x,y+1,depth+1])
      if r_direction == 2 or 4:
        pos.append([x+1,y+1,depth+1])
  
    if maze[x-1,y] == 2 and maze[x+1,y] == 0 and maze[x+1,y] != 9:#下に進む
      pos.append([x+1,y,depth+1])
      maze[x-1,y] = 0
    if maze[x+1,y] == 2 and maze[x-1,y] == 0 and maze[x-1,y] != 9:#上
      pos.append([x-1,y,depth+1])
      maze[x+1,y] = 0
    if maze[x-1,y+1] == 2 and maze[x,y-1] != 9 and maze[x+1,y] != 9:#左下
      pos.append([x+1,y-1,depth+1])
      maze[x-1,y+1] = 0
    if maze[x-1,y-1] == 2 and maze[x,y+1] != 9 and maze[x+1,y] != 9:#右下
      pos.append([x+1,y+1,depth+1])
      maze[x-1,y-1] = 0
    if maze[x+1,y+1] == 2 and maze[x,y-1] != 9 and maze[x-1,y] != 9:#左上
      pos.append([x-1,y-1,depth+1])
      maze[x+1,y+1] = 0
    if maze[x+1,y-1] == 2 and maze[x,y+1] != 9 and maze[x-1,y] != 9:#右上
      pos.append([x-1,y+1,depth+1])
      maze[x+1,y-1] = 0
    if maze[x,y+1] == 2 and maze[x,y-1] != 9:#左
      pos.append([x,y-1,depth+1])
      maze[x,y+1] = 0
    if maze[x,y-1] == 2 and maze[x,y+1] != 9:#右
      pos.append([x,y+1,depth+1])    
      maze[x,y-1] = 0

if __name__ == '__main__':
  #迷路作成
  maze = np.full([25,18],9)
  maze[1:-1,1:-1] = 0

  direction = [1,2,3,4,5]
  r_start = random.randint(2,16)
  start = [[1,r_start,0]]
  Maze2(start)
  
