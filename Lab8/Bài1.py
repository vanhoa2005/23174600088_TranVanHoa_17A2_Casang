def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  """Chương trình chính để in ra các số nguyên tố sinh đôi nhỏ hơn 1000."""
  for num in range(3, 1000, 2):
    if is_prime(num) and is_prime(num + 2):
      print(f"{num}, {num + 2}")

if __name__ == "__main__":
  main()
