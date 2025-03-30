## Adding two float nnumbers
import math

def add_two_numbers(a: float, b: float) -> int:
  return math.floor(a+b)

if __name__ == '__main__':
  a = float(input())
  b = float(input())
  print(add_two_numbers(a, b))