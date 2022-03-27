class Calculator:
    def __init__(self):
        pass

    def helper(self, array):
        current = 0
        sign = '+'
        stack = []
        while len(array) > 0:
            # print(current, stack, sign)
            value = array.pop(0)
            if value == ' ':
                continue
            if value.isdigit():
                current = current * 10 + int(value)
            elif value == '(':
                current = self.helper(array)
            elif value == '+' or value == '-' or value == '*' or value == '/' or value == ')':
                if sign == '+':
                    stack.append(current)
                elif sign == '-':
                    stack.append(-current)
                elif sign == '*':
                    stack[-1] = stack[-1] * current
                else:
                    stack[-1] = stack[-1] / current
                sign = value
                current = 0
                if value == ')':
                    break
        if current:
            if sign == '+':
                stack.append(current)
            elif sign == '-':
                stack.append(-current)
            elif sign == '*':
                stack[-1] = stack[-1] * current
            else:
                stack[-1] = stack[-1] / current

        return sum(stack)

    def solve(self, string):
        self.list = [i for i in string]
        return self.helper(self.list)


cal = Calculator()
test = "((23*4/2+41)/2+33) -31/3"
print(cal.solve(test))
print(eval(test))
