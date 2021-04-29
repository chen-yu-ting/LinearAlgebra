import sys

#矩陣相乘
def MatrixMultiplication(_matrix1, _matrix2):
  row = len(_matrix1)
  col = len(_matrix2[0])
  matrix = [[0 for i in range(col)] for j in range(row)]
  
  for r in range(row):
    for n in range(col):
      sum = 0
      for c in range(col):
        sum += _matrix1[r][c] * _matrix2[c][n]
      matrix[r][n] = sum
  return matrix

#輸入矩陣
def InputMatrix(_row, _col):
  matrix = []
  for r in range(_row):
    matrix.append(list(map(int, input().split())))
    if(len(matrix[r]) != _col):
      sys.exit("您所輸入的資料筆數有誤,與您輸入的矩陣維度不符!")
  return matrix
      
#輸入矩陣維度
print("===輸入第一個矩陣維度===")
matrixDimension_1 = list(map(int, input().split()))
print("===輸入第二個矩陣維度===")
matrixDimension_2 = list(map(int, input().split()))

#判斷矩陣是否能夠相乘
if (matrixDimension_1[1] == matrixDimension_2[0]):
  #輸入矩陣
  print("=====輸入第一個矩陣=====")
  matrix_1 = InputMatrix(matrixDimension_1[0], matrixDimension_1[1])
  print("=====輸入第二個矩陣=====")
  matrix_2 = InputMatrix(matrixDimension_2[0], matrixDimension_2[1])

  #矩陣相乘
  print("======矩陣相乘結果======")
  matrixMultiplicationResult = MatrixMultiplication(matrix_1, matrix_2)
  print(matrixMultiplicationResult)
  
else:
  print("矩陣維度有誤,兩矩陣無法相乘!")


'''      Test data
    ===輸入第一個矩陣維度===
    3 2
    ===輸入第二個矩陣維度===
    2 2
    =====輸入第一個矩陣=====
    8 5
    20 13
    2 1
    =====輸入第二個矩陣=====
    1 0
    2 3
    ======矩陣相乘結果======
    [[18, 15], [46, 39], [4, 3]]
'''
