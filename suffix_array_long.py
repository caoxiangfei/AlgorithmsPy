# python3
import sys

def builds(s):
  sl = [None for _ in range(len(s))]
  for i in range(len(s)):
    if s[i] == 'A':
      sl[i] = 1
    elif s[i] == 'C':
      sl[i] = 2
    elif s[i] == 'G':
      sl[i] = 3
    elif s[i] == 'T':
      sl[i] = 4
    else:
      sl[i] = 0
  return sl

def sortcharacters(sl):
  n = len(sl)
  order = [None for _ in range(n)]
  count = [0, 0, 0, 0, 0]
  string = []

  for i in range(n):
    count[sl[i]] = count[sl[i]] + 1

  temp = count[0]
  for j in range(1, 5):
    if count[j] != 0:
      count[j] = count[j] + temp
      temp = count[j]

  down = list(range(n))
  down.reverse()
  for i in down:
    c = sl[i]
    count[c] = count[c] - 1
    order[count[c]] = i
  return order

def computecharclasses(sl, order):
  n = len(sl)
  cla = [None for _ in range(n)]
  cla[order[0]] = 0
  for i in range(1, n):
    if sl[order[i]] != sl[order[i-1]]:
      cla[order[i]] = cla[order[i-1]] + 1
    else:
      cla[order[i]] = cla[order[i-1]]
  return cla


def sortdoubled(sl, l, order, cla):
  n = len(sl)
  count = [0 for _ in range(n)]
  neworder = [None for _ in range(n)]
  for i in range(n):
    count[cla[i]] = count[cla[i]] + 1
  for j in range(1, n):
    count[j] = count[j] + count[j-1]
  down = list(range(n))
  down.reverse()
  for i in down:
    start = (order[i]-l+n)%n
    cl = cla[start]
    count[cl] = count[cl] - 1
    neworder[count[cl]] = start
  return neworder


def updatecla(neworder, cla, l):
  n = len(neworder)
  newcla = [None for _ in range(n)]
  newcla[neworder[0]] = 0
  for i in range(1, n):
    cur = neworder[i]
    prev = neworder[i-1]
    mid = cur + l
    midprev = (prev + l)%n
    if cla[cur] != cla[prev] or cla[mid] != cla[midprev]:
      newcla[cur] = newcla[prev]+1
    else:
      newcla[cur] = newcla[prev]

  return newcla


def build_suffix_array(text):
  n = len(text)
  sl = builds(text)
  order = sortcharacters(sl)
  cla = computecharclasses(sl, order)
  l = 1
  while l < n:
    order = sortdoubled(sl, l, order, cla)
    cla = updatecla(order, cla, l)
    l = 2 * l

  #result = []
  #for start in order:
    #result.append(text[start:])
  # Implement this function yourself
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
#s = 'GAGAGAGA$'
#sl = builds(s)
#order = sortcharacters(sl)
#cla = computecharclasses(sl, order)
#print(order)
#print(cla)
#print(build_suffix_array(s))