def arithmetic_arranger(opers, output=False):
    x = []
    y = []
    z = []
    a = []

    if len(opers) <= 5:
        for oper in opers:
            if "+" in oper:
                op = "+"
                temp = oper.split(op)
            elif "-" in oper:
                op = "-"
                temp = oper.split(op)
            else:
                return "Error: Operator must be '+' or '-'."
            
            val1 = temp[0].strip()
            val2 = temp[1].strip()
            val1_len = len(val1)
            val2_len = len(val2)
            if val1_len <= 4 and val2_len <= 4:
                try:
                    val1 = str(int(val1))
                    val2 = str(int(val2))
                    if val1_len >= val2_len:
                        val3 = val1_len - val2_len
                        x.append((" " * 2) + val1)
                        y.append(op+" " + (" " * val3) + val2)
                        z.append("-" * (val1_len + 2))
                        if op == "+":
                            za = int(subtract(add(val1_len, 2), len(str(add(val1, val2)))))
                            a.append((" " * za) + add(val1, val2))
                        else:
                            za = int(subtract(add(val1_len, 2), len(str(subtract(val1, val2)))))
                            a.append((" " * za) + subtract(val1, val2))
                    else:
                        val3 = val2_len - val1_len
                        x.append((" " * (2 + val3)) + val1)
                        y.append(op+" " + val2)
                        z.append("-" * (val2_len + 2))
                        if op == "+":
                            za = int(subtract(add(val2_len, 2), len(str(add(val1, val2)))))
                            a.append((" " * za) + add(val1, val2))
                        else:
                            za = int(subtract(add(val2_len, 2), len(str(subtract(val1, val2)))))
                            a.append((" " * za) + subtract(val1, val2))
                except ValueError as er:
                    return "Error: Numbers must only contain digits."
            else:
                return "Error: Numbers cannot be more than four digits."

        if output:
            return ((" " * 4).join(x)+"\\n"+(" " * 4).join(y)+"\\n"+(" " * 4).join(z)+"\\n"+(" " * 4).join(a)).strip()

        return ((" " * 4).join(x)+"\\n"+(" " * 4).join(y)+"\\n"+(" " * 4).join(z)).strip()
    else:
        return "Error: Too many problems."

def add(num1, num2):
  return str(int(num1) + int(num2))

def subtract(num1, num2):
  return str(int(num1) - int(num2))
