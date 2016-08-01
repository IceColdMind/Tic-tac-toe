tic ={'T-L' : ' ',
      'T-C' : ' ',
      'T-R' : ' ',
      'M-L' : ' ',
      'M-C' : ' ',
      'M-R' : ' ',
      'B-L' : ' ',
      'B-C' : ' ',
      'B-R' : ' '}
      
advanced_grid =[
                [tic['T-L'],tic['T-C'],tic['T-R']],
                [tic['M-L'],tic['M-C'],tic['M-R']],
                [tic['B-L'],tic['B-C'],tic['B-R']]
                ]


                
def print_grid(grid):
    print(grid['T-L']+'|'+grid['T-C']+'|'+grid['T-R'])
    print('-+-+-')
    print(grid['M-L']+'|'+grid['M-C']+'|'+grid['M-R'])
    print('-+-+-')
    print(grid['B-L']+'|'+grid['B-C']+'|'+grid['B-R'])


i=0      
while i < 9:
  print('Put the row (top,bot,mid) ( blank for finish) (or display to show the grid)')
  row=str(input())

  x=0
  y=0
  if row == 't':
      x='T'
  elif row == 'b':
      x='B'
  elif row == 'm':
      x='M'
  elif row == '':
      break
  elif row == 'display':
    print_grid(tic)
    continue
    
  else:
    print('Try again please')
    continue
  print('Put the collumn(left,center,right)')
  collumn=input()
  if collumn == 'left':
      y='L'
  elif collumn == 'right':
      y='R'
  elif collumn == 'center':
      y='C'
  else:
    print('There are no right or wrong answers here, but you are wrong!')
    continue
  coord = x + '-' + y
  if tic[coord]==' ' :   
      if i%2==0:
        tic[coord]= 'X'
      else:
        tic[coord]= 'O'
  else:
      print('Box already checked')
      continue
  i+= 1
else:
  print('Game over, all boxes filled')
  
  
