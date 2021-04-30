import sys

#矩陣轉置
def Transpose(_matrix):
  row = len(_matrix)
  col = len(_matrix[0])
  matrix = [[0 for r in range(row)] for c in range(col)]
  for c in range(col):
    for r in range(row):
      matrix[c][r] = _matrix[r][c]
  return matrix

#輸入矩陣
def InputMatrix(_row, _col):
  matrix = []
  for r in range(_row):
    matrix.append(list(map(int, input().split())))
    if(len(matrix[r]) != _col):
      sys.exit("您所輸入的資料筆數有誤,與您輸入的矩陣維度不符!")
  return matrix

print("=====請輸入矩陣維度=====")
matrixDimension = list(map(int, input().split()))
print("=======請輸入矩陣=======")
matrix = InputMatrix(matrixDimension[0], matrixDimension[1])
print("======矩陣轉置結果======")
matrixTransposeResult = Transpose(matrix)
for r in range(len(matrixTransposeResult)):
  print(matrixTransposeResult[r])


'''       Test data 1
    =====請輸入矩陣維度=====
    3 2
    =======請輸入矩陣=======
    2 3
    1 4
    5 6
    ======矩陣轉置結果======
    [2, 1, 5]
    [3, 4, 6]
'''
'''       Test data 2
    =====請輸入矩陣維度=====
    3 3
    =======請輸入矩陣=======
    1 -2 4
    3 7 0
    -5 8 6
    ======矩陣轉置結果======
    [1, 3, -5]
    [-2, 7, 8]
    [4, 0, 6]
'''
