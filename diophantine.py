def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def extended_gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0
  if a >= b:
      if b == 0:
          d, x, y = a, 1, 0
      else:
          (d, p, q) = extended_gcd(b, a % b)
          x = q
          y = p - q * (a // b)

      assert a % d == 0 and b % d == 0
      assert d == a * x + b * y
      return (d, x, y)
  else:
      temp = a
      a = b
      b = temp
      if b == 0:
          d, x, y = a, 1, 0
      else:
          (d, p, q) = extended_gcd(b, a % b)
          x = q
          y = p - q * (a // b)

      assert a % d == 0 and b % d == 0
      assert d == a * x + b * y
      return (d, y, x)

def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    # return (x, y) such that a * x + b * y = c
    d, x, y = extended_gcd(a, b)
    x = x * c / d
    y = y * c / d
    return (x, y)

print(extended_gcd(1, 1))
