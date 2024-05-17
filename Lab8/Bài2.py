def permutation(n, r):
  if r > n:
    return 0
  
  if r == 0:
    return 1
  
  return n * permutation(n - 1, r - 1)

def combination(n, r):
  if r > n:
    return 0
  
  if r == 0 or r == n:
    return 1
  
  return combination(n - 1, r - 1) + combination(n - 1, r)

def main():
  n = int(input("Nhập số lượng phần tử: "))
  r = int(input("Nhập số lượng phần tử lấy ra: "))

  print("Số hoán vị:", permutation(n, r))
  print("Số tổ hợp:", combination(n, r))

if __name__ == "__main__":
  main()
