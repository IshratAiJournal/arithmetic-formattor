ef arithmetic_arranger(problems, show_answers=False):

    # ---------- 1. Validation ----------
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for prob in problems:
        parts = prob.split()
        if len(parts) != 3:
            return 'Error: Incorrect format.'

        num1, op, num2 = parts[0], parts[1], parts[2]

        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # ---------- 2. Width + dash ----------
        width = max(len(num1), len(num2)) + 2
        line1.append(num1.rjust(width))
        line2.append(op + num2.rjust(width-1))
        line3.append('-' * width)

        # ---------- 3. Answer line ----------
        if show_answers:
            ans = str(int(num1) + int(num2) if op == '+' else int(num1) - int(num2))
            line4.append(ans.rjust(width))

    # ---------- 4. Assemble ----------
    arranged = '    '.join(line1) + '\n' + \
               '    '.join(line2) + '\n' + \
               '    '.join(line3)

    if show_answers:
        arranged += '\n' + '    '.join(line4)

    return arranged
