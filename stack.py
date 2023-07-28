# Define the Node class for the singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Stack class using singly linked list
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.data

# Helper function to check if a character is an operand (digit or letter)
def is_operand(char):
    return char.isalnum()

# Helper function to check the precedence of operators
def precedence(operator):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_map.get(operator, 0)

# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    output = []
    stack = Stack()

    for char in expression:
        if is_operand(char):
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '(' from the stack
        else:  # Operator encountered
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                output.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

# Function to convert infix expression to prefix
def infix_to_prefix(expression):
    # Reverse the expression and swap '(' with ')' and vice versa
    reversed_expression = expression[::-1]
    reversed_expression = reversed_expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    prefix_expression = infix_to_postfix(reversed_expression)
    return prefix_expression[::-1]

# Function to evaluate a postfix expression
def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if is_operand(char):
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()

# Function to evaluate a prefix expression
def evaluate_prefix(expression):
    # Reverse the expression
    reversed_expression = expression[::-1]
    stack = Stack()

    for char in reversed_expression:
        if is_operand(char):
            stack.push(int(char))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()

# Test the implementation
if __name__ == "__main__":
    infix_expression = "3+4*2/(1-5)^2^3"
    postfix_expression = infix_to_postfix(infix_expression)
    prefix_expression = infix_to_prefix(infix_expression)

    print("Infix Expression:", infix_expression)
    print("Postfix Expression:", postfix_expression)
    print("Prefix Expression:", prefix_expression)

    postfix_result = evaluate_postfix(postfix_expression)
    prefix_result = evaluate_prefix(prefix_expression)

    print("Postfix Evaluation Result:", postfix_result)
    print("Prefix Evaluation Result:", prefix_result)
