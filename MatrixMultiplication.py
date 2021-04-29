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
matrixDimension = []
print("===輸入第一個矩陣維度===")
matrixDimension.append(list(map(int, input().split())))
print("===輸入第二個矩陣維度===")
matrixDimension.append(list(map(int, input().split())))

#判斷矩陣是否能夠相乘
if (matrixDimension[0][1] == matrixDimension[1][0]):
  #輸入矩陣
  print("=====輸入第一個矩陣=====")
  matrix_1 = InputMatrix(matrixDimension[0][0], matrixDimension[0][1])
  print("=====輸入第二個矩陣=====")
  matrix_2 = InputMatrix(matrixDimension[1][0], matrixDimension[1][1])

  #矩陣相乘
  print("======矩陣相乘結果======")
  matrixMultiplicationResult = MatrixMultiplication(matrix_1, matrix_2)
  print(matrixMultiplicationResult)
  
else:
  print("矩陣維度有誤,兩矩陣無法相乘!")
