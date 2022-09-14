#!/usr/bin/python3

import sys, threading


sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    if self.n < 2:
      return True
    else:
      self.result = []
      node = 0
      current = node
      stack = []  # initialize stack
      #done = 0
    while True:

        # Reach the left most Node of the current Node
        if current != -1:
          if (self.left[current] != -1 and self.key[current] > self.key[self.left[current]] ) or \
                  (self.left[current] == -1 ):
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
            current = self.left[current]
          else:
            return False

          # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif (stack):
          current = stack.pop()
          self.result.append(self.key[current])  # Python 3 printing
          if len(self.result) > 1 and self.result[-2] > self.result[-1]:
            return False

          # We have visited the node and its left
          # subtree. Now, it's right subtree's turn
          current = self.right[current]

        else:
          break

          #re = self.result[-2] > self.result[-1]










    # Finish the implementation
    # You may need to add a new recursive method to do that


def IsBinarySearchTree(tree):
  result = tree.inOrder()
  #print(tree.inOrder())
  if result == False:
    return False
  else:
    return True



  # Implement correct algorithm here



def main():
  tree = TreeOrders()
  tree.read()
  #for i in range(nodes):
    #tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
