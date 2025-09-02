# Evaluate a Postfix Expression
# written by saurabh

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():  # check if it's an integer (handles negative too)
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # truncates towards 0
    return stack[0]

# -------- Testing --------
print(evaluate_postfix("2 1 + 3 *"))   # 9 → ((2+1) * 3)
print(evaluate_postfix("4 13 5 / +")) # 6 → (4 + (13/5))
print(evaluate_postfix("10 6 9 3 + -11 * / * 17 + 5 +")) # 22 (LeetCode example)
