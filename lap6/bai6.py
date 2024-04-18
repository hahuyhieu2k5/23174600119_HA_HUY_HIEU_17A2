#########6.1
def input_matrix(rows, cols):
    matrix = []
    print("Nhập các phần tử của ma trận:")
    for i in range(rows):
        row = []
        for j in range(cols):
            num = float(input(f"Nhập phần tử [{i+1}][{j+1}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

if is_symmetric(matrix):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")




####6.2
 # Kiểm tra đối xứng

def is_invertible(matrix):
  """
  Kiểm tra xem ma trận có khảo nghịch hay không.

  Args:
    matrix: Ma trận cần kiểm tra.

  Returns:
    True nếu ma trận khảo nghịch, False nếu không.
  """
  determinant = np.linalg.det(matrix)
  return determinant != 0
