def arithmetic_arranger(problems, solve=False):

    first_operands = []
    operators = []
    second_operands = []
    results = []
    max_lengths = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Problem format incorrect. Expected 'number operator number'."

        num1_str = parts[0]
        operator = parts[1]
        num2_str = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1_str.isdigit() or not num2_str.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1_str) > 4 or len(num2_str) > 4:
            return "Error: Numbers cannot be more than four digits."

        num1 = int(num1_str)
        num2 = int(num2_str)

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        
        current_max_len = max(len(num1_str), len(num2_str))
        
        first_operands.append(num1_str)
        operators.append(operator)
        second_operands.append(num2_str)
        results.append(str(result)) # Store result as string for formatting
        max_lengths.append(current_max_len)

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in range(len(problems)):
        padding = max_lengths[i] + 2 # +2 for operator and space

        line1.append(first_operands[i].rjust(padding))
        line2.append(operators[i] + second_operands[i].rjust(padding - 1))
        line3.append("-" * padding)
        
        if solve:
            line4.append(results[i].rjust(padding))

    arranged_output = "    ".join(line1) + "\n" + \
                      "    ".join(line2) + "\n" + \
                      "    ".join(line3)

    if solve:
        arranged_output += "\n" + "    ".join(line4)

    return arranged_output
