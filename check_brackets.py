# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]



def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([i, next])

        if next in ")]}":
            # Process closing bracket, write your code here
            opening_brackets_stack.append([i, next])
        if len(opening_brackets_stack) == 1 and (opening_brackets_stack[0][1] in ")]}"):
            return opening_brackets_stack[0][0]
        if len(opening_brackets_stack) > 1 and are_matching(opening_brackets_stack[-2][1], opening_brackets_stack[-1][1]) == True:
            opening_brackets_stack.pop()
            opening_brackets_stack.pop()
        if len(opening_brackets_stack) > 1 and are_matching(opening_brackets_stack[-2][1], opening_brackets_stack[-1][1]) == False and opening_brackets_stack[-1][1] in  ")]}":
            return opening_brackets_stack[-1][0]

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0][0]
    return 'Success'



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
