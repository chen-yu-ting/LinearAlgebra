import sys

#基本列運算
def ElementaryRowOperation(_row, _col, _nowRow, _nowCol, _matrix):
  #領先壹(leading one)
  tmpC = _nowCol
  leadingVariables = _matrix[_nowRow][_nowCol]
  while(tmpC < _col):
    _matrix[_nowRow][tmpC] /= leadingVariables
    tmpC += 1
  #print(_matrix[_nowRow])

  #前向階段(forward phase)
  for r in range(_nowRow + 1, _row):
    if(_matrix[r][_nowCol] != 0):
      nMatrix = [e * -_matrix[r][_nowCol] for e in _matrix[_nowRow]]
      _matrix[r] = [nMatrix[i] + _matrix[r][i] for i in range(_col)]
      #print(_matrix)

  #反向階段(backward phase)
  for r in range(_nowRow - 1, -1, -1):
    if(_matrix[r][_nowCol] != 0): 
      nMatrix = [e * -_matrix[r][_nowCol] for e in _matrix[_nowRow]]
      _matrix[r] = [nMatrix[i] + _matrix[r][i] for i in range(_col)]
      #print(_matrix)    
  #print(_matrix)
  return _matrix

#高斯喬登消去法  
def GaussJordanElimination(_row, _col, _matrix):
  completedRow = []
  for c in range(_col):
    for r in range(_row):
      if(r in completedRow):
        continue
      if(_matrix[r][c] != 0):
        _matrix = ElementaryRowOperation(_row, _col, r, c, _matrix)
        completedRow.append(r)
      elif(_matrix[r][c] == 0):
        for row in range(_row - 1, r, -1):
          if(_matrix[row][c] != 0):
            copyMatrix = _matrix
            for col in range(c, _col):
              tmpM = _matrix[r][col]
              _matrix[r][col] = _matrix[row][col]
              _matrix[row][col] = tmpM
            #print(_matrix)
            _matrix = ElementaryRowOperation(_row, _col, r, c, _matrix)
            completedRow.append(r)
            break
  return _matrix
 
#輸入矩陣
def InputMatrix(_row, _col):
  matrix = []
  for r in range(_row):
    matrix.append(list(map(int, input().split())))
    if(len(matrix[r]) != _col):
      sys.exit("您所輸入的資料筆數有誤,與您輸入的矩陣維度不符!")
  return matrix

print("==========請輸入矩陣維度==========")
matrixDimension = list(map(int, input().split()))

print("===========請輸入您矩陣===========")
matrix = InputMatrix(matrixDimension[0], matrixDimension[1])

print("=====高斯喬登消去法之運算結果=====")
resultMatrix = GaussJordanElimination(matrixDimension[0], matrixDimension[1], matrix)
for r in range(len(matrix)):
  print(resultMatrix[r])
  
 
'''             Test data 1
    ==========請輸入矩陣維度==========
    3 6
    ===========請輸入您矩陣===========
    0 0 -2 0 7 12
    2 4 -10 6 12 28
    2 4 -5 6 -5 -1
    =====高斯喬登消去法之運算結果=====
    [1.0, 2.0, 0.0, 3.0, 0.0, 7.0]
    [0.0, 0.0, 1.0, 0.0, 0.0, 1.0]
    [0.0, 0.0, 0.0, 0.0, 1.0, 2.0]
'''
'''             Test data 2
    ==========請輸入矩陣維度==========
    3 4
    ===========請輸入您矩陣===========
    1 1 2 9
    2 4 -3 1
    3 6 -5 0
    =====高斯喬登消去法之運算結果=====
    [1.0, 0.0, 0.0, 1.0]
    [0.0, 1.0, 0.0, 2.0]
    [0.0, 0.0, 1.0, 3.0]
'''

