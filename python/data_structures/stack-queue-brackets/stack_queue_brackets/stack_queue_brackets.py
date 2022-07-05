from .node import Node
from .stack import Stack


def multi_bracket_validation(string):
    # 0. Create a stack.
    bracket_stack = Stack()
    # 1. Iterate through the string.
    for char in string:
        # 2. If it comes across a (, {, or [, stick on stack.
        if char == "(" or char == "{" or char == "[":
            # Push char to top of stack.
            bracket_stack.push(char)
        # 3. If it comes across a ), }, or ], peek at top of stack.
        if char == ")" or char == "}" or char == "]":
            if bracket_stack.is_empty():
                return False
            match_char = bracket_stack.peek()
            # A. If top of stack is a match, pop the top of the stack and move to next character in string.
            if char == ")" and match_char == "(" or \
                    char == "}" and match_char == "{" or \
                    char == "]" and match_char == "[":
                bracket_stack.pop()
            # B. If top of stack is not a match, return False.
            else:
                return False
    # 4. If at end of string, check if stack is empty.
    if bracket_stack.is_empty():
        # A. If stack is empty, return True.
        return True
        # B. If stack is not empty, return False.
    else:
        return False
