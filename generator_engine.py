from constants import (FOR, WHILE, IF, ELSE, ELIF, RANGE, IMPORT, FROM, WITH, PRINT, BREAK,
                       CONTINUE, ARITHEMATIC_OPERATORS, DEF)


class AlgoGenerator:
    def get_value_between_brackets(self, line):
        i, j = 0, len(line) - 1
        bracket_start, bracket_end = i, j
        bracket_start_found, bracket_end_found = False, False
        while i < j:
            if bracket_start_found and bracket_end_found:
                break
            if not bracket_start_found and line[i] == '(':
                bracket_start = i
                bracket_start_found = True
            elif not bracket_end_found and line[j] == ')':
                bracket_end = j
                bracket_end_found = True
            if not bracket_start_found:
                i += 1
            if not bracket_end_found:
                j -= 1

        return line[bracket_start + 1:bracket_end]


    def handle_loop(self, loop_type, line):
        line = line.lstrip()
        message, start = None, 0
        if loop_type == FOR:
            if RANGE in line:
                iterator = line.split()[1]
                value = self.get_value_between_brackets(line)
                if "," in value:
                    start = int(value.split(",")[0])
                    iterations = int(value.split(",")[1]) - start
                else:
                    iterations = value

                return "Start a for-loop {} times with iterator '{}' starting from {}".format(iterations, iterator, start)
            else:
                return "Start a for-loop on the iterable '{}' with iterator(s) '{}'".format(line.split("in")[1][:-1].strip(), line.split("in")[0].replace("for", "").strip())
        elif loop_type == WHILE:
            condition = line[5:-1]
            return "Run a while-loop with condition {}".format(condition)


    def handle_assignment(self, line):
        if "==" not in line and "=" in line:
            if line[line.index("=") - 1] in ARITHEMATIC_OPERATORS:
                operator = line[line.index("=") - 1]
                operand = line[:line.index("=") - 1].strip()
                if operator == '+':
                    operation = "Increment"
                elif operator == '-':
                    operation = "Decrement"
                elif operator == '/':
                    operation = "Divide"
                elif operator == '*' and line[line.index("=") - 2] == '*':
                    operation = "Raise"
                    operand = line[:line.index("=") - 2].strip()
                elif operator == '*':
                    operation = "Multiply"
                elif operator == '%':
                    operation = "Modulo"

                return "{} the value of '{}' by {}".format(operation, operand, line.split("=")[1].strip())
            return "Set the value of '{}' to '{}'".format(line.split('=')[0].strip(), line.split('=')[1].strip())


    def get_the_value_to_print(self, line):
        value = self.get_value_between_brackets(line)
        if value[0] == "'" or value[0] == '"':
            return "Print {}".format(value)
        else:
            return "Print the value of '{}'".format(value)


    def handle_function_definition(self, line):
        function_name = line.lstrip().split("(")[0][4:]
        params = self.get_value_between_brackets(line)
        return "Define a function '{}' with parameter(s) '{}'".format(function_name, params)


    def get_keyword(self, line):
        keyword = None
        line = line.lstrip()

        if line[:3] == FOR and line[3] == " ":
            keyword = FOR
        elif line[:5] == WHILE and line[5] == " ":
            keyword = WHILE
        elif line[:2] == IF and line[2] == " ":
            keyword = IF
        elif line[:4] == ELIF and line[4] == " ":
            keyword = ELIF
        elif line[:4] == ELSE and line[4] == ":":
            keyword = ELSE
        elif line[:4] == FROM and line[4] == " ":
            keyword = FROM
        elif line[:6] == IMPORT and line[6] == " ":
            keyword = IMPORT
        elif line[:4] == WITH and line[4] == " ":
            keyword = WITH
        elif line[:5] == PRINT and line[5] == "(":
            keyword = PRINT
        elif line[:8] == CONTINUE:
            keyword = CONTINUE
        elif line[:5] == BREAK:
            keyword = BREAK
        elif line[:3] == DEF and line[3] == " ":
            keyword = DEF

        return keyword
